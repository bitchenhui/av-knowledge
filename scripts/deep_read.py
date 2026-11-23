#!/usr/bin/env python3
"""深度精读阶段：glm-5.3 强档消费 deep_read 候选 → 产出 docs/auto/ 长文精读笔记。

流程：
  1. 从 kb/items/papers/ 选 assessment.decision=deep_read 且尚无 deep_dive 的 items
  2. 复用 paper/ 中已有 PDF 或在临时目录中读取原文
  3. pymupdf 抽取全文
  4. 用同主线/共实体的已有 items 作为「与其他论文的联系」素材
  5. 生成与 docs/ 手工精读同构的笔记 → docs/auto/{arxiv_id}.md
  6. 回写 item 的 summaries.deep_dive，跑基底校验

v1 说明：纯文本深读（不提取论文插图）；笔记为自动档，与手工精读分目录存放。

用法：
  uv run --with pyyaml --with pymupdf python scripts/deep_read.py --limit 2
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.request
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from llm_review import LLM  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
KB = ROOT / "kb"
ITEMS = KB / "items" / "papers"
DOCS_AUTO = ROOT / "docs" / "auto"
PAPER_DIR = ROOT / "paper"
CONFIG = ROOT / "config" / "llm.local.yaml"

DEEP_INSTRUCTIONS = """你是音视频/图像编码领域的资深研究员，为领域信息整合引擎撰写论文精读笔记。
要求：
- 忠实原文：所有量化结论必须来自论文文本，带口径（锚点/数据集/条件）；不确定的数字不写。
- 中文、技术密度高：面向该领域研究者，直击方法机理与工程含义，不写科普腔。
- 用全文中标注的 PDF 页码定位方法和主要结果，格式为 [p.7]。仅在正文能支持时，用 Mermaid 表示流程，不要推断看不到的图像内容。
- 笔记全文控制在 6000-9000 字：方法机理写透，实验节保留关键行与结论数字，不逐表抄录。
- 输出 markdown，遵循给定结构，七个小节完整写完。"""

DEEP_INSTRUCTIONS_GENERIC = """你是音视频技术交叉方向的资深研究员，为领域信息整合引擎撰写论文精读笔记
（论文属于非核心大类，按其自身领域的技术标准来评估与解读，并与音视频技术上下游的关联写清楚）。
要求：
- 忠实原文：所有量化结论必须来自论文文本，带口径（锚点/数据集/条件）；不确定的数字不写。
- 中文、技术密度高：面向该领域研究者，直击方法机理与工程含义，不写科普腔。
- 用全文中标注的 PDF 页码定位方法和主要结果，格式为 [p.7]。仅在正文能支持时，用 Mermaid 表示流程，不要推断看不到的图像内容。
- 笔记全文控制在 6000-9000 字：方法机理写透，实验节保留关键行与结论数字，不逐表抄录。
- 输出 markdown，遵循给定结构，七个小节完整写完。"""

NOTE_TEMPLATE = """# {title}

> {authors}. *arXiv:{external_id} ({pub})*
> 本笔记由引擎自动深读生成（glm-5.3, pipeline deep_read v1），底稿：全文文本

## 1. 背景与动机

## 2. 方法总览

## 3. 关键设计

## 4. 实验结果
（有表格数据时用 markdown 表格呈现关键行）

## 5. 消融要点

## 6. 贡献与启示

## 7. 与其他论文的联系
（仅基于下方「相关论文清单」中有真实关联的条目；没有就不写这一节）
"""


def load_yaml(p: Path):
    return yaml.safe_load(open(p, encoding="utf-8"))


def download_pdf(url: str, dest: Path) -> bool:
    if dest.exists() and dest.stat().st_size > 10240:
        return True
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "LLM-Reading-fetcher/0.1"})
            with urllib.request.urlopen(req, timeout=120) as resp:
                dest.write_bytes(resp.read())
            return dest.stat().st_size > 10240
        except Exception as e:  # noqa: BLE001
            print(f"    [下载失败 {type(e).__name__}] 第 {attempt} 次，60s 后重试", flush=True)
            time.sleep(60)
    return False


def read_source(item):
    """Return text and provenance, keeping new PDFs outside the Git tree."""
    import fitz

    ext = item["source"]["external_id"]
    if not re.fullmatch(r"[0-9]{4}\.[0-9]{4,5}(v[0-9]+)?", ext):
        raise ValueError("unsupported arXiv identifier: " + ext)
    url = f"https://arxiv.org/pdf/{ext}"
    with tempfile.TemporaryDirectory(prefix="avk-paper-") as cache:
        pdf = PAPER_DIR / f"{ext}.pdf"
        if not pdf.is_file():
            pdf = Path(cache) / "source.pdf"
            if not download_pdf(url, pdf):
                raise ValueError("PDF download failed")
        digest = hashlib.sha256(pdf.read_bytes()).hexdigest()
        with fitz.open(pdf) as doc:
            pages = len(doc)
            parts = [f"===== 第 {i + 1}/{pages} 页 =====\n{page.get_text()}" for i, page in enumerate(doc)]
    return "\n".join(parts)[:400_000], url, pages, digest


def link_source_pages(note, url, pages, digest):
    """Only link cited pages that actually exist in this PDF version."""
    citations = re.compile(r"\[p\.(\d+)\]")
    refs = [int(n) for n in citations.findall(note)]
    if not refs or any(n < 1 or n > pages for n in refs):
        raise ValueError("missing or out-of-range PDF page reference")
    cited = citations.sub(lambda m: f"[p.{m[1]}]({url}#page={m[1]})", note)
    return f"{cited}\n\n[原文 PDF]({url}) · {pages} 页 · SHA-256 `{digest}`\n"


def checked_card(card, url, pages, digest):
    if (not isinstance(card, dict) or set(card) != {"method", "findings", "limitation"}
            or not all(isinstance(card[k], str) and card[k].strip() for k in ("method", "limitation"))
            or not isinstance(card["findings"], list) or not card["findings"]
            or not all(isinstance(f, str) and f.strip() for f in card["findings"])):
        raise ValueError("invalid paper evidence card")
    for claim in [card["method"], *card["findings"]]:
        refs = re.findall(r"\[p\.(\d+)\]", claim)
        if not refs or any(not 1 <= int(n) <= pages for n in refs):
            raise ValueError("card claim needs an in-range source page")
    source_pages = sorted({int(n) for n in re.findall(r"\[p\.(\d+)\]", " ".join([card["method"], *card["findings"]]))})
    card.update(review_status="model_extracted", source_sha256=digest,
                source_locations=[f"{url}#page={n}" for n in source_pages])
    return card


def finish_note(response, url, pages, digest):
    # The evidence card and the human-readable note come from the same read.
    block = re.search(r"^```paper-evidence[ \t]*\n(.*?)\n```\s*\Z", response.strip(), re.M | re.S)
    if not block:
        raise ValueError("missing paper evidence card")
    card = checked_card(json.loads(block[1]), url, pages, digest)
    return link_source_pages(response[:block.start()].strip(), url, pages, digest), card


def related_items(item: dict, all_items: list[dict], top: int = 8) -> list[dict]:
    mine_ents = {e["ref"] for e in item["entities"]}
    mine_lines = set(item.get("research_lines", []))

    def affinity(o: dict) -> tuple[int, str]:
        if o["id"] == item["id"]:
            return (-1, "")
        shared = mine_ents & {e["ref"] for e in o["entities"]}
        lines = len(mine_lines & set(o.get("research_lines", [])))
        rel = {"high": 3, "medium": 2, "low": 1}.get(o["assessment"]["relevance"], 0)
        return (len(shared) * 2 + lines + rel, o["id"])

    cands = sorted(all_items, key=affinity, reverse=True)[:top]
    return [c for c in cands if affinity(c)[0] > 0]


def build_prompt(item: dict, fulltext: str, related: list[dict]) -> str:
    src, meta = item["source"], item["time"]
    rel_list = "\n".join(
        f"- {r['id']}｜{r['title']}｜{r['summaries'].get('one_liner_zh', '')}"
        for r in related) or "（无）"
    header = NOTE_TEMPLATE.format(
        title=item["title"],
        authors=", ".join(item.get("_authors", ["（见原文）"])),
        external_id=src["external_id"],
        pub=meta["published"],
    )
    return f"""请为以下论文撰写精读笔记，直接输出 markdown 笔记本体（从一级标题开始），结构与示例如下：

{header}

方法和主要结果都请写出 [p.N] 页码。笔记末尾另附一个 fenced code block，首行是 ```paper-evidence，内为有效 JSON 对象，键包括 method（一句方法，含 [p.N]）、findings（一个或多个含 [p.N] 的结果，每项写清适用条件）、limitation（一句对适用范围的说明）。以单独一行三个反引号结束。

相关论文清单（第 7 节只能从中选确有真实关联的，写清关联依据）：
{rel_list}

论文全文：
{fulltext}"""


def make_reading(llm, item, text, url, pages, digest, all_items):
    if item["summaries"].get("deep_dive"):
        prompt = ("只读这份带页码的论文，输出有效 JSON 对象，键为 method、findings、limitation。"
                  "method 用一句话说清输入、主要操作、输出并用 [p.N] 标出出处。"
                  "findings 是字符串列表，每条写明实验条件、结果和 [p.N]，只摘录经原文支持的结论。"
                  "limitation 写适用边界。请用中文，保留技术符号。\n" + text)
        response = llm.chat(prompt, tier="deep", instructions="从公开论文制作可核对的证据卡。", max_tokens=8000).strip()
        if response.startswith("```json\n") and response.endswith("\n```"):
            response = response[8:-4]
        return None, checked_card(json.loads(response), url, pages, digest)
    instructions = (DEEP_INSTRUCTIONS if item.get("domain", "video_image_coding") == "video_image_coding"
                    else DEEP_INSTRUCTIONS_GENERIC)
    response = llm.chat(build_prompt(item, text, related_items(item, all_items)), tier="deep",
                        instructions=instructions, max_tokens=30000).strip()
    if response.startswith("```markdown\n") and response.endswith("\n```"):
        response = response[len("```markdown\n"):-4].strip()
    return finish_note(response, url, pages, digest)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=2)
    args = ap.parse_args()

    cfg = load_yaml(CONFIG)
    llm = LLM(cfg)
    all_items = [load_yaml(p) | {"_path": p} for p in sorted(ITEMS.glob("*.yaml"))]

    cands = [d for d in all_items
             if (d["assessment"]["decision"] == "deep_read"
                 or d["assessment"]["relevance"] == "high")
             and (not d["summaries"].get("deep_dive") or not d["summaries"].get("research_brief"))]
    # 引用量优先（5 年回补的"只读高引精华"策略），引用缺失按 0 处理
    for d in cands:
        q = ROOT / "queue" / "papers" / f"{d['id'].split(':')[-1]}.yaml"
        try:
            d["_cit"] = (yaml.safe_load(open(q, encoding="utf-8")) or {}).get("citation_count") or 0
        except Exception:  # noqa: BLE001
            d["_cit"] = 0
    cands.sort(key=lambda d: (not d["summaries"].get("deep_dive"), d["_cit"],
                              {"high": 2, "medium": 1, "low": 0}[d["assessment"]["relevance"]],
                              d["time"]["published"]), reverse=True)
    cands = cands[: args.limit]
    print(f"deep_read 候选 {len(cands)} 篇（本次处理）\n")
    if not cands:
        print("无候选（全部已深读或无 deep_read 判定）——正常退出")
        return 0

    today = date.today().isoformat()
    n_ok = 0
    for item in cands:
        arxiv_id = item["id"].split(":")[-1]
        print(f"[{arxiv_id}] {item['title'][:60]}")
        try:
            text, url, pages, digest = read_source(item)
        except Exception as exc:
            print(f"    ✗ 原文读取失败: {exc}")
            continue
        print(f"    PDF {pages} 页，全文输入 {len(text)} 字符")

        # 队列里存过作者信息；item 里没有，从 queue 补
        q = ROOT / "queue" / "papers" / f"{arxiv_id}.yaml"
        if q.exists():
            item["_authors"] = load_yaml(q).get("meta", {}).get("authors", [])
        try:
            note, card = make_reading(llm, item, text, url, pages, digest, all_items)
        except Exception as exc:
            print(f"    ✗ 精读或原文定位失败: {exc}")
            continue
        if note is not None:
            note_path = DOCS_AUTO / f"{arxiv_id}.md"
            DOCS_AUTO.mkdir(exist_ok=True)
            note_path.write_text(note, encoding="utf-8")
            item["summaries"]["deep_dive"] = str(note_path.relative_to(ROOT))
        print(f"    → 证据页 {card['source_locations']}")
        item["summaries"]["research_brief"] = card
        item["time"]["updated"] = today
        item.pop("_authors", None)
        item.pop("_path", None)
        item.pop("_cit", None)
        yaml.safe_dump(item, open(ITEMS / f"{arxiv_id}.yaml", "w", encoding="utf-8"),
                       allow_unicode=True, sort_keys=False, width=100)
        n_ok += 1
        # all_items 里的副本也更新，供后续论文做 related
        for d in all_items:
            if d["id"] == item["id"]:
                d["summaries"]["deep_dive"] = item["summaries"]["deep_dive"]

    print(f"\n完成 {n_ok}/{len(cands)}；tokens in={llm.usage['in']} out={llm.usage['out']}")
    if n_ok:
        print("\n运行基底校验：")
        return subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_kb.py")]).returncode
    return 1


if __name__ == "__main__":
    sys.exit(main())
