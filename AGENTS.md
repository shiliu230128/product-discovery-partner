# AGENTS.md

## 项目使命

Product Discovery Partner 是一个证据驱动的产品发现 Skill。它帮助用户：

1. 判断一个产品想法是否真实、值得做。
2. 找到第一批用户和最窄可验证切口。
3. 判断技术、AI、商业和合规上的可行性与风险。
4. 在写规格之前做出 CONTINUE / NARROW / PIVOT / PAUSE / STOP 的决策。
5. 输出与当前证据匹配的产物，而不是默认写完整 PRD。

一句话定位：

> 先判断该不该做，再决定做什么，最后才写规格。

## 核心原则

- 证据优先于自述。兴趣不是需求；E0 不能升级为已验证。
- 决策优先于文档。PRD 是条件产物，不是流程终点。
- 最窄切口优先于完整平台。MVP 是最小可验证价值。
- 诚实优先于讨好。尊重用户，但不把假设写成事实。
- 区分用户已确认、助手推断、助手建议和待确认。
- 技术建议服务产品阶段、团队能力和风险，不追求“先进”。

## Skill 行为摘要

- 开始会话时先选深度：快速（约 8 问）、标准（15–20 问）、深度（30+ 问）。
- 默认一次问一个高价值问题。
- 维护 8 个槽位：问题、用户、证据、价值与切口、流程、MVP 与非目标、技术与 AI、商业与决策。
- 维护证据账本：E0–E3、来源、状态、置信度。
- 支持跳转、回填、存档、恢复；上游改变时标记下游为 stale。
- 在关键检查点和写 PRD 前运行决策门。
- 输出四层产物：决策备忘、精简 PRD、完整 PRD、build spec。
- 验证必须闭环：假设 → 测试 → 阈值 → 结果回写 → 新决策。
- 外部研究必须引用来源；没有联网能力时明确降级，不编造。

## 文件结构

```text
product-discovery-partner/
  SKILL.md                         # 核心行为，保持精简
  references/
    interview-engine.md            # 深度档位、8 槽位、跳转/回填/存档
    evidence-ledger.md             # 证据等级、来源、矛盾处理
    decision-gate.md               # 决策门、五种出口、kill criteria
    validation-playbook.md         # 访谈提纲、fake door、concierge、结果回写
    research-playbook.md           # 竞品/市场/监管扫描、引用规则
    output-contract.md             # 四层产物、章节选择器、质量检查
    discovery-question-bank.md     # 问题库
    product-sense-playbook.md      # 产品判断
    tech-stack-playbook.md         # 技术栈
    ai-product-playbook.md         # AI 产品
    market-context-cn.md           # 中国市场可选模块
    examples.md                    # 多轮示例
    outputs/                       # 四种产物模板
    en/                            # 英文翻译
    i18n-manifest.json             # 翻译源文件哈希
  scripts/check-i18n.py            # 双语一致性检查
  evals/evals.json                 # 轻量行为用例
  demo/sample-run.md               # 新流程样例
```

## 开发规则

### 中文是 canonical source

- 修改行为、规则、模板时，先改中文文件。
- 再更新 `references/en/` 对应文件。
- 最后运行：

```bash
cd product-discovery-partner
python3 scripts/check-i18n.py --update
python3 scripts/check-i18n.py
```

`--update` 只应在确认英文翻译已经同步后运行。它记录中文源文件的 SHA-256，用于检测漂移。

### SKILL.md 保持精简

- 只放核心行为、模式、决策门、输出合同和参考文件加载规则。
- 长模板、问题库、示例放到 `references/`。
- 不要把 25 节 PRD 模板塞回 SKILL.md。

### 不默认写完整 PRD

- 快速档默认输出决策备忘。
- 标准档默认输出精简 PRD。
- 完整 PRD 只在决策门 CONTINUE 且用户明确需要时输出。
- PAUSE/STOP 时不要写完整 PRD。

### 每个关键判断都要有状态

使用统一标签：

- `[已验证 F-01]`
- `[假设 A-01]`
- `[猜测 G-01]`
- `[待确认 Q-01]`
- `[外部来源 R-01]`

### 反讨好

- 赞美证据，不赞美想法。
- 每个重要建议写最强反方论据。
- 问“什么会改变你的判断？”
- 用户坚持时要求新证据，不因投入多而退让。
- 允许输出 STOP。

## 当前范围与已知缺口

已实现：

- 自适应访谈、三档深度、8 槽位。
- 证据账本、状态标签、矛盾处理。
- 决策门和 kill criteria。
- 验证包与结果回写。
- 四层产物模板。
- 中国市场和 AI 合规模块。
- 双语同步检查。

暂未实现：

- 盲评 A/B 质量评测。
- Python 自动跑分 harness。
- 真实脱敏访谈回归集。
- 拆分为多个可组合 Skill。

不要声称现有 evals 能证明质量优势。它只覆盖基础行为。

## 修改后的检查清单

- [ ] `SKILL.md` 是否仍然精简、可执行？
- [ ] 新增/修改的规则是否同时更新了英文翻译和 manifest？
- [ ] `python3 scripts/check-i18n.py` 是否通过？
- [ ] `evals/evals.json` 是否是有效 JSON？
- [ ] 是否没有默认写完整 PRD 的倾向？
- [ ] 是否保留了 PAUSE/STOP 出口？
- [ ] 是否没有把假设写成事实？
- [ ] 是否没有回到 10 阶段线性问卷？

## 许可与归属

本项目基于 MIT License。原始项目归属和修改声明见 `NOTICE.md` 与 `LICENSE`。不要删除原始 MIT 版权声明；新增内容版权归 shiliu。

## 安全边界

涉及公众人物、声音、身份、金融、医疗、法律、儿童、政治内容或高风险自动化时，必须尽早提出安全、授权、标识、合规和人工确认问题。详见 `product-discovery-partner/SAFETY.md`。
