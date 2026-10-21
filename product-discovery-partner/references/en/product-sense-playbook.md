# Product Judgment Playbook

Product judgment is not about making the user's words sound better. It is about compressing vague wishes into testable facts, then making tradeoffs from those facts.

## 1. Judgment Priorities

1. Real demand evidence, not just interest.
2. A specific user and the cost of the status quo.
3. The narrowest testable wedge.
4. Explicit non-goals.
5. Technical and operational feasibility.
6. Observable success metrics and kill criteria.

## 2. Evidence Over Self-Report

Interest is not demand. Signals vary in strength:

- Weak (E0): finds it interesting, willing to try, joins a waitlist, friends say it is good.
- Medium (E1): willing to show a real workflow, agrees to a second interview, can describe a specific recent problem.
- Strong (E2): shares real data, repeats a workaround, multiple independent users have the same problem.
- Stronger (E3): pays, prepays, brings in a team, replaces an existing process, would be upset if the product disappeared.

If you only have E0, do not expand features. Design a cheap test or mark the conclusion as an assumption.

## 3. Users Must Be Specific and Reachable

“SMBs,” “product managers,” “creators,” and “young people” are still too broad. Narrow to:

- Role: who, on what team, reporting to whom.
- Scenario: when, and why now.
- Task: what result they need.
- Pressure: what happens if they fail.
- Budget: who pays, and how much.
- Success criteria: what “done” means.
- Reach: where to find the first 20 users.

A good user profile tells you where to find the first users and why they would try now.

## 4. Problem Quality

Judge whether a problem is worth solving:

- Frequency: daily, weekly, monthly, or yearly?
- Severity: time, money, revenue, risk, emotion, or coordination cost?
- Is there already a forcing function: compliance, deadline, customer complaint, revenue loss?
- Has the user actively searched for a solution?
- Why is the current solution insufficient?
- If nothing is done, will the user keep hurting, or can they live with it?

High-frequency small pain and low-frequency severe pain can both work, but the product and GTM differ. Do not replace frequency and cost with “it hurts.”

## 5. The Status Quo Is the Real Competitor

The real competitor is usually the status quo, not another product.

Ask:

- What does the user do today?
- Which tools do they stitch together?
- Who handles it manually?
- How much time is wasted per week?
- What happens when it goes wrong?
- Why have they not switched yet?
- What is the switching cost: data, habit, training, integration, procurement?

If the user says “there is no solution,” be careful: it may be an opportunity, or the problem may not be painful enough.

## 6. Value Proposition

Strong value usually comes from:

- A clear time saving.
- A clear reduction in errors.
- A clear revenue increase.
- A clear risk reduction.
- A capability that was previously impossible.
- Turning complex work into a simple process.

Weak value often sounds like:

- “A bit more convenient.”
- “A better experience.”
- “Maybe someone will use it.”
- “Lots of features.”
- “It uses AI.”

The value proposition must answer: what is the specific moment the user first feels it is worth it?

## 7. MVP and the Narrowest Wedge

An MVP is not the fewest features. It is the smallest testable value.

Order of judgment:

1. What is the user's most painful moment?
2. Which action proves they truly need it?
3. Which features are required to complete that action?
4. Which features only make the experience more complete?
5. Which features slow down validation?
6. Can you deliver the result before delivering the system?
7. Can you use manual work, a semi-automated process, no-code tools, or an existing API?

A narrow wedge can be:

- A weekly report.
- One automation.
- An insight card.
- A review flow.
- An export.
- A small-team workflow.
- A concierge delivery.

Do not chase a full platform early. Prove that one narrow loop can be used repeatedly.

## 8. Non-Goals

What you will not do is as important as what you will do.

Non-goals should state:

- Which users v1 does not serve.
- Which channels/platforms are out of scope.
- Which automation is not included.
- Which quality level is not promised.
- Which features are deferred to V1/V2.

An MVP without non-goals usually becomes a smaller copy of the full product, and validation takes longer.

## 9. Retention and Business Model

Ask where retention comes from:

- Data accumulation.
- Team collaboration.
- Recurring tasks.
- Content updates.
- Business results.
- Workflow lock-in.
- Network effects.

A product without a retention source tends to become a one-off tool.

Common business models:

- B2B subscription: ongoing value and team use.
- Usage-based: AI, automation, APIs, data processing.
- Take rate: marketplaces.
- Service fee: early high-ticket validation.
- Freemium: user scale and self-propagation.

Pricing should connect to value. Do not only ask “is it expensive?” Ask whether the price is reasonable relative to time saved, losses avoided, or revenue created.

## 10. Metrics

Metrics should connect to user value, not vanity.

- North Star Metric: the observable behavior that shows the user gets core value.
- Activation: the first time the user experiences value.
- Retention: why the user comes back.
- Conversion/payment: whether the user will spend money or organizational resources.
- Quality: error rate, human correction rate, satisfaction.
- Guardrail: metrics that must not be sacrificed for growth, such as complaints, refunds, and safety incidents.

If you could watch only three metrics after 30 days, choose the three that best prove “users truly need this.”

## 11. Risk Judgment

Identify at least:

- Demand risk: is the pain real?
- Solution risk: does this approach actually work?
- Technical risk: can the core capability meet the quality bar?
- Distribution risk: where do users come from?
- Retention risk: why do users come back?
- Business risk: who pays, and how much?
- Compliance/safety risk: is there an unacceptable issue?

Risks should be written as testable assumptions, not generic “the market is competitive.”

## 12. Anti-Sycophancy

- Praise evidence, not ideas.
- Write the strongest counter-case for every important recommendation.
- Ask “what would change your judgment?”
- When the user pushes back, ask for new evidence; do not cave because they have invested effort.
- Separate the person from the idea.
- Do not use “this is a great idea” as a transition.
- Do not use a full PRD to hide a “do not build” judgment.

## 13. Common Failure Modes

- Treating “often” as high frequency without asking for count.
- Treating a waitlist as demand.
- Treating a competitor's feature list as user demand.
- An MVP too large to validate in 2–4 weeks.
- Writing goals but no non-goals.
- Metrics such as signups or page views instead of user value.
- No kill criteria.
- Being unable to stop because the user has invested effort.
- Wrapping a traditional rules/process problem in AI.
- Treating “technically possible” as “product-wise worth doing.”

## 14. Quick Product-Type Checks

### AI Product

Ask first whether AI is necessary, what errors cost, what quality threshold matters, where human confirmation sits, and what it costs. Do not start with “which model.”

### Marketplace

Ask who comes first on each side, how trust is built, how payments/disputes work, and where cold start begins. Technology is not the biggest risk.

### Internal Tool

Ask about workflow, permissions, exception handling, audit logs, and adoption friction. A pretty UI is not the core.

### B2B SaaS

Ask about user/buyer/decision-maker, procurement, security/permissions, integrations, and renewal reasons.

### Mobile App

Ask about entry frequency, notifications, offline use, system permissions, and app-store review. Do not default to native.

### Regulated Product

Ask about licenses/filings, data, content moderation, human review, and risk tiers. Compliance may change the product scope.
