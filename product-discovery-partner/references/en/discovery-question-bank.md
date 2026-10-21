# Product Discovery Question Bank

Use this file only to choose the next highest-value question. Do not dump the whole bank on the user.

## 1. The Eight Quick-Mode Questions

Quick mode decides whether the idea is worth pursuing. It does not produce a full PRD.

1. **Trigger:** What specific moment made you think of this product?
2. **User:** Who feels the pain most? Who uses it, who pays, and who decides?
3. **Status quo:** How do they solve it today? How much time or money does the workaround cost per week?
4. **Evidence:** What is the strongest evidence you have seen: real behavior, payment, an artifact, or verbal interest?
5. **Wedge:** If you could produce one smallest result that would make one user use or pay this week, what would it be?
6. **Non-goals:** What will v1 explicitly not do?
7. **Implementation:** Should v1 be web, mobile, a mini program, an extension, a bot, or API-first? Are there hard technical or compliance constraints?
8. **Decision:** If you could watch only three metrics after 30 days, which three? What result would make you stop?

End with a decision memo. Do not automatically write a full PRD.

## 2. Standard-Mode Additions

Add:

- The complete current workflow.
- Which step is most error-prone, slowest, or least trusted.
- Why users have not switched yet.
- The first moment the product feels worth it.
- The core path and two failure paths.
- P0/P1/non-goals.
- Tech stack, data sources, permissions, integrations.
- Business model, first 100 users, retention source.
- The biggest risk assumption and how to test it.

## 3. Deep-Mode Additions

Add:

- Are user, buyer, decision-maker, and influencer different? What is the procurement process?
- Competitors, substitutes, pricing, channels, and market changes.
- Regulation, filings, data, content moderation, compliance.
- System architecture, async jobs, permission boundaries, audit.
- AI eval set, quality thresholds, human confirmation, rollback.
- Admin and exception handling.
- Multi-stage roadmap and kill criteria.

## 4. Questions by Slot

### Problem and Trigger

- When did this problem last happen? What exactly happened?
- How often does it happen? What was the worst consequence?
- If unsolved, what is lost: time, money, revenue, risk, emotion, coordination efficiency?
- Did this idea come from personal experience, a customer request, market observation, or technical inspiration?

### User and Buyer

- Who feels the pain most? Who uses it, who pays, who decides?
- What kind of user would try an imperfect early version?
- Where can you find the first ten users? Can you reach them directly?
- What are the user's role, goals, budget, success criteria, and cost of failure?
- If user, buyer, and decision-maker differ, what motivates each?

### Evidence and Current Workaround

- What exactly does the user do today? Which tools? Who handles it manually?
- How much time or money does the workaround cost per week/month?
- What is the strongest evidence: payment, prepayment, real data, workflow dependency, or verbal interest?
- Has the user actively looked for a solution? What did they try, and why did they stop?
- Who would be genuinely upset if this product disappeared tomorrow? Why?
- Will any user show you a real spreadsheet, screenshot, ticket, or chat log?

### Value and Wedge

- What is the first moment the user feels it is worth it?
- Does the product make users faster, cheaper, more professional, safer, or capable of something new?
- If a competitor copied 80% of the features, what advantage remains?
- Why now? What changed in technology, policy, platforms, or user behavior?
- If you could deliver one result instead of a system, what would it be?

### Flow and Experience

- On first entry, should the user see a result, a task, data, or onboarding?
- What steps complete the core task?
- Where are users most likely to abandon or lose trust?
- How do empty, loading, error, permission-denied, and recovery states work?
- Are notifications, collaboration, history, export, or sharing needed?

### MVP and Non-Goals

- If you could build only three features to validate value, which three?
- Which tempting features should be explicitly excluded?
- What is the MVP success bar: core action, repeated use, payment, or business outcome?
- Can you validate manually, semi-manually, with no-code tools, or an existing API?
- What is the smallest version someone would pay for, reuse, or depend on?
- If users did not need to log in or integrate anything, what value could they still get?

### Technology and AI

- Should v1 be web, mobile, mini program, desktop, extension, bot, or API-first?
- What does the team know best? Budget, launch date, expected scale?
- Is AI necessary? Is it core value or an efficiency layer?
- What are the AI inputs and outputs? Which results must be accurate?
- What happens if AI is wrong? Are citations, confidence, human confirmation, or rollback needed?
- Is RAG, an Agent, tool calling, multimodal input, or fine-tuning actually needed?
- Where does data come from? Who can access it? Are real-time collaboration, payments, notifications, admin, integrations, or compliance needed?
- Which technical decisions are reversible, and which are hard to undo?

### Business and Metrics

- Who pays, and why? Is subscription, usage-based, one-time, service fee, or take rate more natural?
- Where do the first 100 users come from?
- Does retention come from data, collaboration, habit, content, or business results?
- What action proves the user experienced value?
- If you could track only three metrics after 30 days, which three?
- Which metric could look good without proving real value?
- What are CAC, average revenue, gross margin, and payback period roughly?

### Risk and Decision

- What is the most likely reason this product fails?
- Which assumption, if wrong, changes the whole direction?
- What is the biggest technical, market, or compliance risk?
- What must be validated before the MVP?
- What result would make you stop or pivot?
- If we do nothing, will users keep feeling real pain, or can they live with it?

## 5. Evidence Follow-Up Questions

When the user gives a vague or weak claim, ask:

- “Is this behavior you observed, or something you inferred?”
- “When did this last happen? Can you walk me through it?”
- “How many people? How many actually invested time, money, or data?”
- “What do they use instead? Why haven't they switched?”
- “Is there a screenshot, spreadsheet, ticket, or chat log I can see?”
- “If the product disappeared tomorrow, who would be genuinely upset?”
- “Is this strong evidence, medium evidence, or just verbal interest?”

## 6. Validation and Decision Questions

- Which assumption, if wrong, should change the current direction?
- What is the cheapest test? Can it be done in 48 hours, one week, or two weeks?
- What is the pass threshold? What is the fail threshold?
- If the result is ambiguous, what next?
- If you had to choose CONTINUE / NARROW / PIVOT / PAUSE / STOP now, which would you choose, and why?
- What evidence would change that judgment?

## 7. Usage Rules

- Ask one question at a time by default.
- Only list a batch when the user asks for one, and mark priorities.
- Avoid empty prompts such as “anything else?”
- Do not ask irrelevant questions just to cover the bank.
- If the user cannot answer, offer 2–3 options and a provisional assumption, then continue.
