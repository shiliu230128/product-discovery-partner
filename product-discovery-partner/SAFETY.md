# 安全与产品边界 / Safety and Product Boundaries

Product Discovery Partner 帮助探索和定义产品。有些想法涉及敏感领域，Skill 应该在 PRD 或 build spec 把它当成实现细节之前，尽早提出风险。

## 中文

### 公众人物、声音与身份

涉及模拟公众人物、角色 Agent、声音、肖像或人格时：

- 不要暗示角色就是真实本人。
- 使用清晰标识，例如“基于公开信息的模拟角色”。
- 避免未经授权的声音克隆。
- 区分历史演绎和事实陈述。
- 尽可能提供来源依据。
- 不要把生成的引语写成真实引语。
- 为在世公众人物、政治人物、明星和普通人定义不同风险等级。
- 定义同意、下架和更正路径。

### 高风险建议

涉及金融、医疗、法律、心理健康、政治说服或雇佣决策时：

- 不要给出确定性的专业建议。
- 把输出定位为框架或教育性支持。
- 在合适时建议咨询专业人士。
- 明确不确定性和局限。
- 对重要动作设计人工确认。
- 为高风险建议保留审计记录。

### AI Agent 动作

如果 AI 产品可以调用工具或执行动作，明确：

- 能做什么。
- 不能做什么。
- 哪些动作需要确认。
- 如何记录每一步。
- 用户如何撤销或恢复。
- 如何限制成本和频率。
- 如何处理提示注入和越权。

高风险动作默认需要人工确认。

### 数据与隐私

尽早询问：

- 收集什么数据？
- 谁可以看？
- 是否敏感？
- 用户是否清楚同意？
- 用户可以导出或删除吗？
- 是否涉及第三方集成？
- 数据是否跨境？
- 保存多久？

### PRD / Build Spec 要求

如果产品涉及敏感领域，最终 PRD 或 build spec 应包含：

- 风险等级。
- 用户可见的披露。
- 数据处理规则。
- 内容边界。
- 升级或人工复核路径。
- 滥用场景。
- 监控需求。
- 不可接受风险的 kill criteria。

### 免责声明

本项目是产品思考辅助工具，不构成法律、医疗、金融或其他专业建议。法规和平台规则会变化，做合规或商业决策前请核实最新官方要求并咨询专业人士。

## English

Product Discovery Partner helps explore and define products. Some ideas involve sensitive domains. The Skill should surface those risks early, before the PRD or build spec treats them as implementation details.

### Public Figures, Voice, and Identity

For products involving simulated public figures, character agents, voice, likeness, or personality:

- Do not imply the character is the real person.
- Use clear labeling such as “simulated character based on public information.”
- Avoid unauthorized voice cloning.
- Distinguish historical interpretation from factual claims.
- Provide source grounding where possible.
- Do not present generated quotes as real quotes.
- Define risk tiers for living public figures, political figures, celebrities, and private individuals.
- Define consent, takedown, and correction paths.

### High-Stakes Advice

For finance, medical, legal, mental health, political persuasion, or employment decisions:

- Do not give definitive professional advice.
- Position outputs as frameworks or educational support.
- Recommend expert consultation where appropriate.
- State uncertainty and limitations.
- Design human confirmation for consequential actions.
- Keep an audit trail for high-risk recommendations.

### AI Agent Actions

If an AI product can call tools or take action, define:

- What it can do.
- What it cannot do.
- Which actions require confirmation.
- How every step is logged.
- How users can undo or recover.
- How cost and rate limits are enforced.
- How prompt injection and privilege escalation are handled.

High-risk actions should default to human confirmation.

### Data and Privacy

Ask early:

- What data is collected?
- Who can see it?
- Is it sensitive?
- Do users clearly consent?
- Can users export or delete their data?
- Are third-party integrations involved?
- Does data cross borders?
- How long is it retained?

### PRD / Build Spec Requirements

If a product touches a sensitive area, the final PRD or build spec should include:

- Risk level.
- User-facing disclosures.
- Data handling rules.
- Content boundaries.
- Escalation or human review paths.
- Abuse cases.
- Monitoring needs.
- Kill criteria for unacceptable risk.

### Disclaimer

This project is a product-thinking aid. It is not legal, medical, financial, or other professional advice. Regulations and platform rules change. Verify current official requirements and consult qualified professionals before making compliance or business decisions.
