# Product Discovery Partner

> 证据驱动的产品发现 Skill：先判断该不该做，再决定做什么，最后才写规格。

Product Discovery Partner 是一个面向创业者、产品经理、独立开发者和 AI 产品团队的 Skill。它不会一上来写 PRD，而是通过自适应访谈、证据账本和决策门，帮你把一个模糊想法推进成可判断、可验证、可执行的产品方案。

## 它和普通 PRD 工具有什么不同

普通 PRD 工具默认“这个想法值得做”，然后把功能写完整。

Product Discovery Partner 先问：

- 这个问题真实吗？频率和成本足够吗？
- 第一批用户是谁？在哪里找到？
- 用户现在怎么解决？为什么还没换？
- 最强的证据是行为、付费、artifact，还是口头兴趣？
- 最小可验证切口是什么？
- 现在应该继续、收窄、转向、暂停，还是停止？

它会明确区分事实、假设、猜测和待确认，并允许输出 `PAUSE` 或 `STOP`。

## 三种深度

| 档位 | 问题预算 | 适用 | 默认产物 |
|---|---|---|---|
| 快速 | 约 8 问 | 早期判断、内部讨论 | 决策备忘 + 关键假设 + 下一步验证 |
| 标准 | 15–20 问 | 准备做 MVP、对齐小团队 | 精简 PRD + 验证包 |
| 深度 | 30+ 问，自适应 | 融资、招聘、高风险产品 | 完整 PRD + build spec + AI 评测集 |

支持随时跳转、回填、存档和恢复。用户不需要按 10 个阶段线性走完。

## 四层产物

- **决策备忘（一页纸 brief）**：判断继续/收窄/转向/暂停/停止，附证据、反方论据和 kill criteria。
- **精简 PRD**：8–10 节，足够开始设计和开发。
- **完整 PRD**：条件产物，按产品类型选章节，不默认写 25 节。
- **Build Spec**：用户故事、验收标准、数据模型、API、权限、AI 评测、测试计划。

假设清单是核心产物，不是附录。所有关键判断都会标注 `[已验证]`、`[假设]`、`[猜测]` 或 `[待确认]`。

## 核心机制

### 证据账本

把证据分成 E0–E3：

- E0：口头兴趣、赞美、等候名单。
- E1：具体过去行为、直接引语、单个真实场景。
- E2：artifact、重复的笨办法、真实时间/数据投入、多个独立用户。
- E3：付费、预付、生产依赖、签约承诺。

E0 不能升级为“已验证”。

### 决策门

在写 PRD 前评估问题证据、用户可触达性、切口可测试性、技术可行性、商业闭环和风险，输出五种结果之一：

```text
CONTINUE / NARROW / PIVOT / PAUSE / STOP
```

### 验证闭环

验证不只是“建议你去聊聊”。它会产出可执行的验证包：假设、测试方式、访谈提纲/fake door 文案、样本、通过/失败阈值，以及结果触发什么决策。用户跑完测试后，可以把结果回写，更新证据和判断。

### 外部研究

可选竞品、市场、定价、渠道和监管扫描。有联网能力时引用 URL 和日期；没有时给出精确搜索词和待填表，绝不编造。

## 安装

把 `product-discovery-partner/` 文件夹复制到本地 Skills 目录：

```text
product-discovery-partner/
  SKILL.md
  README.md
  SAFETY.md
  references/
  scripts/
  evals/
  demo/
```

开启一个新的助手会话，让 Skill 元数据被发现。

如果你要发布或再分发这个 Skill，请把仓库根目录的 `LICENSE` 和 `NOTICE.md` 一起带上。

## 使用

中文：

```text
我有一个产品想法，但还很模糊。请用 product-discovery-partner 的方式，通过提问帮我判断该不该做、怎么做。
```

English:

```text
I have a rough product idea. Use product-discovery-partner to interview me, test the evidence, and tell me whether and how to build it.
```

## 仓库结构

```text
product-discovery-partner/
  SKILL.md
  README.md
  SAFETY.md
  references/
    interview-engine.md
    evidence-ledger.md
    decision-gate.md
    validation-playbook.md
    research-playbook.md
    output-contract.md
    discovery-question-bank.md
    product-sense-playbook.md
    tech-stack-playbook.md
    ai-product-playbook.md
    market-context-cn.md
    examples.md
    outputs/
      decision-memo.md
      lean-prd.md
      full-prd.md
      build-spec.md
    en/
      ... English translations
    i18n-manifest.json
  scripts/
    check-i18n.py
  evals/
    evals.json
  demo/
    sample-run.md
```

## 双语与同步

中文 references 是 canonical source。英文翻译在 `references/en/`。

检查漂移：

```bash
cd product-discovery-partner
python3 scripts/check-i18n.py
```

更新翻译并确认后：

```bash
python3 scripts/check-i18n.py --update
```

脚本会检查文件是否缺失、英文是否为空、标题结构是否一致，以及中文源文件哈希是否与 manifest 匹配。

## 评测

`evals/evals.json` 目前只包含一个轻量行为用例集，检查“是否先问、是否追证据、是否避免过早写 PRD”等行为。它不证明输出质量优于普通助手。

质量对照评测（盲评、A/B、真实脱敏对话回归集）暂未实现，后续再补。计划见 [ROADMAP.md](ROADMAP.md)。

## 安全边界

这个 Skill 用于产品发现和规格撰写，不构成法律、医疗、金融或其他专业建议。涉及公众人物、声音、身份、金融、医疗、法律、儿童、政治内容或高风险自动化时，应在早期提出安全、授权、标识和合规问题。

详见 [SAFETY.md](product-discovery-partner/SAFETY.md)。

## License

MIT License. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).

---

## English Summary

Product Discovery Partner is an agent Skill for evidence-driven product discovery. Instead of jumping to a PRD, it runs an adaptive interview, maintains an evidence ledger, applies a decision gate, and produces the smallest artifact that answers the user's real question: a decision memo, lean PRD, full PRD, or build spec.

It supports quick, standard, and deep modes; jump/backfill/checkpoint/resume; evidence levels E0–E3; a `CONTINUE / NARROW / PIVOT / PAUSE / STOP` decision gate; and a validation loop that writes results back into the evidence ledger.

Chinese references are canonical. English translations live in `references/en/` and are checked with `scripts/check-i18n.py`.

The current eval suite is a small behavior suite, not a quality benchmark. A blind A/B quality evaluation is deferred.

MIT licensed. See `LICENSE` and `NOTICE.md`.
