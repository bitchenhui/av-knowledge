# 标准生态 · 领域综述

> 引擎合成 · 数据截止 2026-11-21 · 基于 1002 条结构化条目 · glm-5.3

# 标准生态 · 领域综述（增量修订版）

> 引擎合成 · 增量修订 · 数据截止 2026-11-15（本版补录 5 条，条目日期 2026-06-25 ～ 2026-10-17）· 全库 1007 条（+5，其中 3 条为上一版已引用条目的结构化全文补录）

# 标准生态（视频编码标准与生态）领域综述

> 数据截止：2026-11-15。本综述基于给定条目（JVET 会议提案、算法描述/草案文本节点、工业动态与论文条目）撰写；条目未覆盖的判断以〔综述推断〕显式标注。本版为增量修订：融合本周补录的 5 条新条目，其余表述继承上一版。

---

## 一、发展历程

以 JVET（ITU-T VCEG + ISO/IEC MPEG 联合组）为主线，2021–2026 年的标准生态可划分为四个阶段，其代际切换遵循“AHG 探索 → EE 探索实验 → CfE → CfP”的程序链条。

### 阶段一：VVC 定稿后的维护与生态奠基（2021-10 ～ 2022）

- **组织形态**：JVET 以常设专题组（AHG1–AHG12）覆盖项目管理、文本编辑、参考软件（VTM）、测试素材、一致性、ECM 软件、HDR/WCG、高位深/高码率/高帧率、SEI、编码优化、神经网络编码（AHG11）、超越 VVC 增强压缩（AHG12）全线工作（standard_proposal:jvet:m188-X0001 ~ m188-X0012）；2022-01 增设胶片颗粒专题组 AHG13（standard_proposal:jvet:m189-Y0013），AHG7 转向低时延与受限复杂度（standard_proposal:jvet:m189-Y0007）。
- **文本节点**：VVC 操作范围扩展草案推进至 Draft 5（standard_proposal:jvet:m188-X2005）、一致性测试 Draft 7（standard_proposal:jvet:m188-X2008）、范围扩展一致性 Draft 2（standard_proposal:jvet:m188-X2026）；VVC v1/v2 一致性测试 BoG 启动（standard_proposal:jvet:m188-X0207）；HEVC 新级别草案 Draft 1→3（standard_proposal:jvet:m188-X1005、m190-Z1005）；AVC/HEVC/视频 CICP 增补色彩类型标识符 Draft 1→4（standard_proposal:jvet:m190-Z1008 ~ m194-AD1008）。跨标准勘误机制每会运行（standard_proposal:jvet:m188-X1004 起系列）。
- **参考软件版本**：VTM 15（standard_proposal:jvet:m188-X2002）→ VTM 17（standard_proposal:jvet:m190-Z2002）→ VTM 18（standard_proposal:jvet:m192-AB2002）；ECM 3（standard_proposal:jvet:m188-X2025）→ ECM 6（standard_proposal:jvet:m191-AA2025）→ ECM 7（standard_proposal:jvet:m192-AB2025）。
- **探索启动**：EE2（超越 VVC 增强压缩）自 2021-10 起每会输出总结（standard_proposal:jvet:m188-X0024、m188-X2024 起系列）；ECM 侧 GDR（standard_proposal:jvet:m189-Y0162、m189-Y0163）、RPR 修复与滤波强化（standard_proposal:jvet:m188-X0121、m190-Z0062、m190-Z0069）密集推进。
- **部署信号**：每会固定发布 HEVC/VVC 部署状态报告（standard_proposal:jvet:m188-X0020、m188-X0021 起系列）；优酷基于 Ali266 的 VVC 流媒体试部署（standard_proposal:jvet:m189-Y0122）、VVenC/VVdeC 持续更新（standard_proposal:jvet:m188-X0044、m189-Y0136）、字节 BVC 异构 CPU+GPU 解码器（standard_proposal:jvet:m189-Y0054）、VVC/HEVC 8K 主观对比（standard_proposal:jvet:m188-X0186）。

### 阶段二：下一代探索机制化与专题扩容（2023）

- **组织扩容**：2023-01 增设 NNVC 软件开发 AHG14（standard_proposal:jvet:m193-AC0014）与面向机器分析（VCM）专题组（standard_proposal:jvet:m193-AC0015）；2023-04 起 AHG7 转为 ECM 工具评估、VCM 落位 AHG8（standard_proposal:jvet:m194-AD0007、m194-AD0008）。
- **ECM 提速与评估体系成型**：ECM 9→11（standard_proposal:jvet:m194-AD2025、m195-AE2025、m196-AF2025）；ECM 主观评估首报（standard_proposal:jvet:m192-AB0270）、ECM/VTM 视觉质量对比（standard_proposal:jvet:m192-AB2029）、分阶段复杂度评估（standard_proposal:jvet:m195-AE0195）、内存消耗系列报告（standard_proposal:jvet:m190-Z0150、m195-AE0180、m196-AF0201）确立“增益+主观+复杂度+内存”四维评估框架。
- **多层 VVC 进入验证测试（VT）**：计划草案（standard_proposal:jvet:m192-AB0123、m192-AB2021）→ 更新 1（standard_proposal:jvet:m195-AE2021）；空间可伸缩性专家观看结果（standard_proposal:jvet:m194-AD0399、m195-AE0288、m196-AF0311）、内容分层报告（standard_proposal:jvet:m196-AF2033）。
- **SEI 与 NN 工具扩张**：Green-MPEG SEI 进 VTM（standard_proposal:jvet:m190-Z0046、m192-AB0072）；SEI 处理顺序消息 Draft 1→6（standard_proposal:jvet:m191-AA2027 ~ m195-AE2027）；NNPF/NNPFC 向 AVC/HEVC 移植（standard_proposal:jvet:m195-AE0101、m196-AF0045）。
- **HEVC 多视点线启动**：苹果提出 HEVC 多视点 Profile（standard_proposal:jvet:m191-AA0239），扩展位深草案 Draft 1→2（standard_proposal:jvet:m191-AA1011、m195-AE296）。
- **外部并行路线**：MPAI-EEV 端到端神经编码标准声称感知指标优于 H.266/VVC（paper:arxiv:2309.07589）；MPEG-5 LCEVC 在 JVET 内对照 HM/VTM 评估并引发多轮交叉验证与异议（standard_proposal:jvet:m196-AF0075、m196-AF0224、m196-AF0228、m196-AF0277、m196-AF0292）。

### 阶段三：应用导向扩张与 CfE 启动（2024 ～ 2025 中）

- **新专题组**：游戏内容压缩 AHG15（standard_proposal:jvet:m197-AG0015）、生成式人脸视频压缩（GFVC）AHG16（standard_proposal:jvet:m197-AG0016）、超越 CTC 测试 AHG17（standard_proposal:jvet:m201-AK0017）、超低时延与丢包韧性 AHG18（standard_proposal:jvet:m202-AL0018）。
- **VVC 版本整合**：第 4 版草案 Draft 8→13（standard_proposal:jvet:m198-AH2005 ~ m203-AM2005）；第 2 版参考软件基线 Draft 1→2（standard_proposal:jvet:m198-AH2009、m200-AJ2009）。
- **ECM 12→20**（standard_proposal:jvet:m197-AG2025 ~ m206-AP2025），配套上下文重训练周期（standard_proposal:jvet:m198-AH0223、m199-AI0281）、工具关断消融（standard_proposal:jvet:m193-AC1711、m193-AC0354）、工具交互分析（standard_proposal:jvet:m202-AL0171）、12 比特内部位深（standard_proposal:jvet:m200-AJ0237、m203-AM0216）。
- **CfE 启动**：2025-03 提出联合 CfE 草案（standard_proposal:jvet:m202-AL0047、m202-AL2026），2025-06 JVET 与 MPEG 联合发布 CfE（standard_proposal:jvet:m203-AM2026）。
- **部署深化**：骁龙 X Elite AI PC 上 4K 120fps VVC 播放（standard_proposal:jvet:m200-AJ0265）、Chromium 播放方案（standard_proposal:jvet:m203-AM0242）、资源受限 4K 超低延迟软件编码演示（standard_proposal:jvet:m203-AM0298）。

### 阶段四：CfE 收束、CfP 发布与组织转段（2025-10 ～ 2026-10）

- **CfE→CfP 闭环**：CfE 修订文本与结果（standard_proposal:jvet:m204-AN2026、m204-AN2029）；多方响应（standard_proposal:jvet:m204-AN0085、m204-AN0198、m204-AN0267）；CfP 草案（standard_proposal:jvet:m205-AO2026、m205-AO0045）→ 最终草案（standard_proposal:jvet:m206-AP2026）→ **2026-07 联合 CfP 正式发布**（standard_proposal:jvet:m207-AQ2021），应征提案描述模板定稿（standard_proposal:jvet:m207-AQ2022、m208-AR2022）。
- **配套基准与口径**：CfE 条件下 ECM/VTM 性能（standard_proposal:jvet:m203-AM0269）、CfE/CfP 用 ECM 基准点（standard_proposal:jvet:m204-AN0272）、CfP VTM 编码规划（standard_proposal:jvet:m206-AP0296）、VTM-24.0 RDO 计数作为 CfP 复杂度报告口径（standard_proposal:jvet:m208-AR0138）、0.2 倍运行时间目标配置（standard_proposal:jvet:m206-AP0237）。
- **组织转段**：ECM 止步于 v20（standard_proposal:jvet:m206-AP2025），其后会议无新版算法描述；2026-10 AHG6 改设为“非参考软件资产”（standard_proposal:jvet:m208-AR0006）——〔综述推断〕ECM 探索线的角色已被 CfP 评估流程取代。**但转段仅限探索线**：同期 HEVC 参考软件 HM 的维护性更新仍推进至 Draft 2（standard_proposal:jvet:m208-AR1017），成熟标准参考软件的例行维护节奏未受组织转段影响。硬件实现复杂度专题组于 2026-01 设立（AHG19，standard_proposal:jvet:m205-AO0019）并于 2026-04 起固化为 AHG16（standard_proposal:jvet:m206-AP0016）。
- **多层 VVC 收口**：VT 计划更新至第 8 版（standard_proposal:jvet:m205-AO2021）、主观观看结果与验证测试报告落地（standard_proposal:jvet:m206-AP0268、m206-AP2033）；MV-HEVC 新档位一致性码流交付（standard_proposal:jvet:m207-AQ0186）。
- **许可生态信号**：WIPO 与 Via Licensing Alliance 合作扩展经专利池验证的 SEP 数据（industry_news:viala:wipo-expands-pool-verified-sep-data-with-via-licensing-allia）；USPTO 局长 Squires 出席 Via LA 十月 Bridge Summit 并发表主题演讲（industry_news:viala:uspto-director-squires-to-deliver-keynote-speech-at-via-lice），池组织与美国专利主管部门的接触升至局长级；Via LA 启动数据中心 DRAM 首个专利池（已有许可方签约并计划再建一池）、任命 Tony Piotrowski 为总法律顾问（industry_news:viala:via-licensing-alliance-formally-launches-first-patent-pool-i、industry_news:viala:via-licensing-alliance-appoints-tony-piotrowski-as-general-c）——数据透明度建设、池模式跨域复制与政策层接触三线并进。

---

## 二、技术主线与代表工作

### 主线 1：VVC 家族的多版本维护与整合
v2（范围扩展/一致性）、第 4 版 Draft 8–13（standard_proposal:jvet:m198-AH2005 ~ m203-AM2005）直至 2025-10 汇入“含扩展与更正的 VVC”新版整合草案 Draft 1（standard_proposal:jvet:m204-AN2001）；一致性规范迭代至 Draft 8（standard_proposal:jvet:m204-AN2008）并启动增补修正草案（standard_proposal:jvet:m202-AL2028）；HM/VTM 通用测试条件（CTC）与软件开发指南形成例行维护（standard_proposal:jvet:m192-AB2010、m201-AK2010、m202-AL2010、m206-AP2010；m193-AC2003、m200-AJ2003）。VVC 结构概念参考指南（standard_proposal:jvet:m204-AN0258）与 MC-IF 技术指南（standard_proposal:jvet:m195-AE0154、m196-AF0175）完善生态知识基线。

### 主线 2：ECM/EE2 超越 VVC 探索
以 ECM 3→20 的版本链为载体，覆盖划分优化与交叉验证（standard_proposal:jvet:m188-X0144、m188-X0196）、模板匹配类帧内工具（standard_proposal:jvet:m191-AA0132、m204-AJ0043、m199-AI0051）、帧间 MTS（standard_proposal:jvet:m190-Z0147）、色度 IBC 回迁（standard_proposal:jvet:m193-AC0080）、GDR（standard_proposal:jvet:m190-Z0118、m190-Z0141）、RPR 编码器控制（standard_proposal:jvet:m196-AF0058、m197-AG0116）、环内滤波（standard_proposal:jvet:m200-AJ0210、m202-AL0225、m203-AM0219）、熵编码上下文与 bin/bit 比率分析（standard_proposal:jvet:m195-AE0147、m203-AM0227、m204-AN0223）。主观验证（standard_proposal:jvet:m198-AH0344、m198-AH2029）与工具消融方法学（standard_proposal:jvet:m193-AC0354）构成证据链。

### 主线 3：神经网络编码三线并进
- **ECM 内嵌 NN 工具**：NN 环路滤波（standard_proposal:jvet:m189-Y0079、m189-Y0098）、NN 帧内预测映射 VVC 模式（standard_proposal:jvet:m192-AB0149、m193-AC0116，三重交叉验证 m193-AC0238、m193-AC0270、m193-AC0298）、CNN 超分+RPR（standard_proposal:jvet:m191-AA0065、m192-AB0077）、统一参考帧合成（standard_proposal:jvet:m199-AI0089、m203-AM0114、m204-AN0084）、轻量多尺度参考帧生成（standard_proposal:jvet:m201-AK0071、m202-AL0104）、NNLF 接口与共享模型评估（standard_proposal:jvet:m201-AK0337、m202-AL0228、m203-AM0176）、张量帧内模式推导进 VTM 与 CfP 响应软件（standard_proposal:jvet:m205-AO0200）。
- **SEI 化 NN 后处理激活存量**：NNPFC 帧率上采样（standard_proposal:jvet:m193-AC0074）、NNPF 扩展 AVC/HEVC（standard_proposal:jvet:m195-AE0101、m196-AF0045）、NNPFC/NNPFA 接口文本（standard_proposal:jvet:m200-AJ0049、m201-AK0053）、VVdeC 实时 NNPF 开源实现（standard_proposal:jvet:m206-AP0130）。
- **端到端学习编解码器入锚**：DCVC-FM / DCVC-RT 作为 EE1 学习型帧内锚点（standard_proposal:jvet:m205-AO0186、m205-AO0191、m206-AP0080，交叉验证 m205-AO0295）。外部 MPAI-EEV 提供非 ITU/ISO 路线对照（paper:arxiv:2309.07589）。

### 主线 4：面向机器与新兴内容
VCM（AHG8）：VVC 工具的机器视觉适用性分析（standard_proposal:jvet:m194-AD0186）、机器消费残差精简（standard_proposal:jvet:m197-AG0217、m198-AH0248）、人机混合消费多层 VVC（standard_proposal:jvet:m197-AG0216、m198-AH0247）；游戏内容（standard_proposal:jvet:m201-AK0081、m201-AK0082）；GFVC（standard_proposal:jvet:m201-AK0068、m202-AL0101）；胶片颗粒（FGC SEI 编辑与网页播放器 standard_proposal:jvet:m198-AH0311、区域特性 SEI 进 VTM TuC standard_proposal:jvet:m203-AM0168）；全息/物波 SEI（standard_proposal:jvet:m195-AE0182、m197-AG0049）；V-PCC 评估指标与承载（standard_proposal:jvet:m193-AC0044、m205-AO0090）。

### 主线 5：HEVC/AVC 存量生态再激活
- HEVC：MV-HEVC 档位（字节跳动+苹果联合提案 standard_proposal:jvet:m197-AG0201，明确空间视频需求）、4:4:4 MV 档位链（standard_proposal:jvet:m199-AI0045、m200-AJ247、m204-AN0293、m206-AP0242）、子图支持（standard_proposal:jvet:m199-AI0256、m206-AP0263、m207-AQ0188）、分层色度推导（standard_proposal:jvet:m200-AJ0215）、新档位/颜色描述符/SEI 草案序列（standard_proposal:jvet:m195-AE1006 ~ m207-AQ1006）、参考软件 HM 维护性更新 Draft 2（standard_proposal:jvet:m208-AR1017）、整合版本草案（standard_proposal:jvet:m204-AN1018 等）、白皮书（standard_proposal:jvet:m199-AI1011、m200-AJ1011）。
- AVC：含扩展与修正的整合草案 Draft 1→6（standard_proposal:jvet:m195-AE1016 ~ m206-AP1016）、附加 SEI 支持 Draft 1→5（standard_proposal:jvet:m201-AK1017 ~ m205-AO1017）、新 SEI 扩展机制（standard_proposal:jvet:m205-AO0212、m205-AO0280）。

### 主线 6：SEI 元数据与治理
绿色元数据、SEI 处理顺序（standard_proposal:jvet:m191-AA2027 系列、HEVC/AVC 移植 m202-AL0210）、SPO/PON 跨规范归属调整（standard_proposal:jvet:m199-AI0146、m204-AN0059）、模态信息 SEI（standard_proposal:jvet:m197-AG0079、m198-AH0049、m201-AK0107）、AI 使用限制（standard_proposal:jvet:m202-AL0062）、数字签名内容（standard_proposal:jvet:m201-AK0194）、目标掩膜/深度/alpha 元数据信令（standard_proposal:jvet:m194-AD0175、m206-AP0229、m206-AP0230）、GSI/显示矩形/打包区域（standard_proposal:jvet:m206-AP0223、m202-AL0138、m202-AL0059）。

### 主线 7：实现部署与许可生态
VVenC/VVdeC（含多层与 NNPF，standard_proposal:jvet:m195-AE0172、m203-AM0239、m206-AP0130）、Ali266（智能手机实时编码与评测 standard_proposal:jvet:m205-AO0221、m206-AP0124）、BVC（直播优化 standard_proposal:jvet:m200-AJ0256）、Ittiam i266 移动部署（standard_proposal:jvet:m206-AP0214）、NHK 广播级多层编码器与浏览器/动态层切换原型（standard_proposal:jvet:m201-AK0274、m207-AQ0190、m207-AQ0191）。许可生态侧：WIPO×Via LA 池验证 SEP 数据合作（industry_news:viala:wipo-expands-pool-verified-sep-data-with-via-licensing-allia）、USPTO 局长 Bridge Summit 主题演讲（industry_news:viala:uspto-director-squires-to-deliver-keynote-speech-at-via-lice）、数据中心 DRAM 首池落地并计划再建一池与总法律顾问任命（industry_news:viala:via-licensing-alliance-formally-launches-first-patent-pool-i、industry_news:viala:via-licensing-alliance-appoints-tony-piotrowski-as-general-c）构成部署经济性侧的持续信号流。

---

## 三、关键问题（开放问题）

**1. CfP 评估的复杂度口径与公平性。** VTM-24.0 RDO 计数被定为 CfP 复杂度报告统一口径（standard_proposal:jvet:m208-AR0138），配合 0.2 倍运行时间目标配置（standard_proposal:jvet:m206-AP0237）与 CfE/CfP 基准点（standard_proposal:jvet:m203-AM0269、m204-AN0272）。RDO 计数是与编码器实现解耦的算子级代理指标，但其向真实实现成本的映射（AHG16 硬件实现复杂度议题，standard_proposal:jvet:m205-AO0019、m206-AP0016）尚无公开校准方法——〔综述推断〕CfP 投标中“软件复杂度排名”与“硬件友好性”可能出现系统性偏离；ECM 时代内存消耗系列（standard_proposal:jvet:m190-Z0150、m195-AE0180、m196-AF0201）提示内存维度在 CfP 口径中的权重是待决问题。

**2. NN 工具的标准形态与互操作边界。** 主线 3 的三线并进留下架构级未决项：模型交付位置（比特流内信令 vs 带外分发）、NNLF 共享模型的跨解码器一致性评估（standard_proposal:jvet:m203-AM0176）尚未形成与一致性测试等同的验证体系；NNPF/NNPFC 移植 AVC/HEVC（standard_proposal:jvet:m195-AE0101、m196-AF0045）要求存量解码路径承载 NN 后处理，目前仅有接口文本（standard_proposal:jvet:m200-AJ0049、m201-AK0053）而无大规模实证；端到端锚点（DCVC-FM/RT，standard_proposal:jvet:m205-AO0186、m205-AO0191，交叉验证 m205-AO0295）与传统锚的可比性依赖单一交叉验证链。〔综述推断〕张量帧内推导进入 CfP 响应软件（standard_proposal:jvet:m205-AO0200）意味着 NN 组件将直接进入下一代测试模型，而模型文件分发、版本与知识产权处置规则尚无公开文本。

**3. 客观指标与主观质量的错配。** LCEVC 对照 HM/VTM 引发的多轮交叉验证与异议（standard_proposal:jvet:m196-AF0075、m196-AF0224、m196-AF0228、m196-AF0277、m196-AF0292）表明增强/后处理类技术在传统率失真指标下存在系统性评价偏差；ECM 主观评估（standard_proposal:jvet:m192-AB0270、m198-AH0344、m198-AH2029）提供方法论雏形，但“主观测试通用条件”（样本量、观看环境、内容分层，参照 standard_proposal:jvet:m196-AF2033）尚未与 CTC 同等制度化。〔综述推断〕若 CfP 响应普遍包含 NN 生成类工具，主观验证的统计功效问题将在下一代标准验证测试中前移（GFVC 专题已是先例）。

**4. SEP 许可环境与部署经济性的信息不对称。** 每会部署状态报告（standard_proposal:jvet:m188-X0020、m188-X0021 起系列）覆盖技术就绪度，但许可成本结构无对等透明度：WIPO×Via LA 池验证 SEP 数据合作（industry_news:viala:wipo-expands-pool-verified-sep-data-with-via-licensing-allia）仅覆盖池内专利；USPTO 局长级出席池组织峰会（industry_news:viala:uspto-director-squires-to-deliver-keynote-speech-at-via-lice）显示政策层关注上升但未触及费率口径。〔综述推断〕下一代标准周期内 SEP 申报与池组建时点将早于 VVC 时代，FRAND 口径的公开化程度是关键观察变量。

**5. 多标准并行的版本治理负担。** VVC/HEVC/AVC 三线“含扩展与更正的整合版本”并行（standard_proposal:jvet:m204-AN2001、m204-AN1018、m195-AE1016 ~ m206-AP1016），跨标准勘误每会运行，HM 参考软件维护性更新推进至 Draft 2（standard_proposal:jvet:m208-AR1017）——规范文本、一致性码流、参考软件三类资产的版本对齐是持续性工程负担；〔综述推断〕整合版本与分立增补并存期间的“现行文本”指认存在规范状态歧义风险，MV-HEVC 一致性码流交付（standard_proposal:jvet:m207-AQ0186）等先行实践可视为对齐模板。

**6. CTC 内容集对新兴内容的代表性。** AHG17（超越 CTC，standard_proposal:jvet:m201-AK0017）的制度化即是对该问题的承认：游戏（standard_proposal:jvet:m201-AK0081、m201-AK0082）、生成式人脸（standard_proposal:jvet:m201-AK0068）、机器消费（standard_proposal:jvet:m197-AG0217）等内容特性与现有 CTC 集分布差异显著；〔综述推断〕CfP 测试条件对这些类别的吸收程度将直接影响下一代标准工具取向（如模板匹配类帧内工具对合成内容的适配性，参照 standard_proposal:jvet:m199-AI0051、m204-AJ0043）。

---

## 四、趋势

**1. 开发模式切换：从共识性探索到竞争性评估。** ECM 止步 v20（standard_proposal:jvet:m206-AP2025）、AHG6 转设“非参考软件资产”（standard_proposal:jvet:m208-AR0006）、2026-07 CfP 发布与应征模板定稿（standard_proposal:jvet:m207-AQ2021、m207-AQ2022、m208-AR2022）——JVET 重启“CfP→测试模型→迭代收敛”的代际路径。〔综述推断〕下一代标准正式开发预计 2027 年启动；ECM 遗产（工具消融 m193-AC0354、上下文重训练 m198-AH0223、m199-AI0281）将以候选技术池形式回流 CfP 响应。

**2. NN 组件由工具层升格为架构层。** 张量帧内模式推导进 CfP 响应软件（standard_proposal:jvet:m205-AO0200）、端到端学习编解码器首次成为正式锚点（standard_proposal:jvet:m205-AO0186、m206-AP0080）、VVdeC 实时 NNPF 开源（standard_proposal:jvet:m206-AP0130）打通存量激活——“混合架构 NN 内嵌 + SEI 后处理激活存量”双轨将同时作用于下一代标准与前代存量。

**3. 码流语义从“为人眼”扩展为“人机共消费”。** VCM 常设化（AHG8）、人机混合多层 VVC（standard_proposal:jvet:m197-AG0216、m198-AH0247）、目标掩膜/深度/alpha 信令（standard_proposal:jvet:m206-AP0229、m206-AP0230）、AI 使用限制 SEI（standard_proposal:jvet:m202-AL0062）——元数据治理（机器消费权限、AI 训练限制）正成为与压缩效率并列的规范内容面。

**4. 存量标准进入“档位/SEI 增量再服务期”。** 空间视频驱动 MV-HEVC 档位与子图链（standard_proposal:jvet:m197-AG0201、m206-AP0263、m207-AQ0188）、AVC 新 SEI 扩展机制（standard_proposal:jvet:m205-AO0212、m205-AO0280）、HM 例行维护延续至 2026-10（standard_proposal:jvet:m208-AR1017）——AVC/HEVC 与 VVC 在 XR/直播/广播场景形成互补分工而非线性替代。

**5. 部署就绪度领先于生态迁移。** 解码硬件（骁龙 X Elite 4K 120fps，standard_proposal:jvet:m200-AJ0265）、浏览器路径（Chromium，standard_proposal:jvet:m203-AM0242）、移动实时编码（Ali266，standard_proposal:jvet:m205-AO0221、m206-AP0124）与广播级多层（NHK，standard_proposal:jvet:m207-AQ0190、m207-AQ0191）全栈就绪；〔综述推断〕瓶颈集中于内容供给、编码成本与许可确定性，而非技术可用性。

**6. SEP 生态制度化提速：数据透明、池扩张与政策接触三线并进。** WIPO×Via LA 池验证 SEP 数据扩展（industry_news:viala:wipo-expands-pool-verified-sep-data-with-via-licensing-allia）建设透明度基础设施；数据中心 DRAM 首池落地且已有许可方签约、并计划再建一池（industry_news:viala:via-licensing-alliance-formally-launches-first-patent-pool-i）显示池模式向视频编码之外复制；USPTO 局长 Squires 出席 Via LA 十月 Bridge Summit（industry_news:viala:uspto-director-squires-to-deliver-keynote-speech-at-via-lice）与 Tony Piotrowski 出任总法律顾问（industry_news:viala:via-licensing-alliance-appoints-tony-piotrowski-as-general-c）显示池组织治理与政策层接触同步加深——〔综述推断〕专利治理与标准开发的耦合度上升，下一代标准周期内池组建时点与费率透明度将成为部署决策的一级变量。

---

## 本周演进

1. **新增｜许可生态出现“政策层接触”维度**：USPTO 局长 Squires 确认在 Via LA 十月 Bridge Summit 发表主题演讲（industry_news:viala:uspto-director-squires-to-deliver-keynote-speech-at-via-lice）。此前该线仅有数据合作（WIPO）与商业扩张（新池、人事）信号，本条首次出现美国专利主管部门局长级官员与池组织的公开互动——趋势 6 中“政策接触加深”由〔综述推断〕升级为有据结论；已写入阶段四“许可生态信号”、主线 7 与关键问题 4。

2. **新增｜HEVC 存量维护线的参考软件本体证据**：HM 维护性更新 Draft 2（standard_proposal:jvet:m208-AR1017，2026-10 会议）补上上一版缺失的参考软件维护记录。此前 HEVC 维护证据链以规范文本草案（1005/1006 系列）与 CTC/开发指南（2010/2003 系列）为主；本条确认在 ECM 停版（standard_proposal:jvet:m206-AP2025）与 AHG6 转设（standard_proposal:jvet:m208-AR0006）之后，AR 会议的存量标准软件维护照常运转——**强化**“存量互补而非替代”判断（趋势 4），并为关键问题 5 的“文本-码流-软件版本对齐”论点补入直接证据；已在阶段四组织转段处补充澄清（探索线停更 ≠ 软件线全线停更）。

3. **补录确认｜三条 Via LA 条目入库，无结论变化**：WIPO SEP 数据合作（industry_news:viala:wipo-expands-pool-verified-sep-data-with-via-licensing-allia）、DRAM 首池（industry_news:viala:via-licensing-alliance-formally-launches-first-patent-pool-i）、Piotrowski 任命（industry_news:viala:via-licensing-alliance-appoints-tony-piotrowski-as-general-c）上一版已引用并纳入正文，本次为结构化条目全文补录（条目日期早于上一版数据截止，属回溯入库），相关表述与结论维持不变。

4. JVET 技术线（CfP 流程、NN 编码、SEI/档位草案）本周无新条目，该部分无实质演进。
