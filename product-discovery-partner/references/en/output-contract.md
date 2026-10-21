# Output Contract

This file defines when to produce which artifact. The default is not “write a full PRD.” The default is “answer the question the user actually has.”

## 1. Four Output Tiers

| Tier | Artifact | Purpose | When to use | Length |
|---|---|---|---|---|
| L0 | Decision memo (one-page brief) | Decide whether to build, continue, or stop | Quick mode, decision gate returns PAUSE/STOP, user asks “is this worth doing?” | 1–2 pages |
| L1 | Lean PRD | Align a small team, prepare an MVP | Standard mode, decision gate returns CONTINUE/NARROW | 5–10 pages |
| L2 | Full PRD | Fundraising, hiring, multi-team coordination, complex products | Decision gate returns CONTINUE and the user explicitly needs it | 10–25 pages, section-selected |
| L3 | Build Spec | Hand to a coding agent or engineering team | Ready to build, need acceptance criteria and data model | Organized by module |

Do not default to L2 just because the user says “write a PRD.” First decide whether they need a decision, alignment, or execution.

## 2. Decision Gate Before Output

Before any L1/L2/L3, there must be a decision gate result.

- CONTINUE: proceed to L1/L2/L3.
- NARROW: narrow the scope first, then produce L1.
- PIVOT: present alternative paths before writing a PRD for the current direction.
- PAUSE: produce L0 + a validation pack. Do not write a full PRD.
- STOP: produce L0, explain why, and do not write a PRD.

If the user insists on a PRD, you may write one, but you must:

- Mark it at the top as “a draft based on unverified assumptions.”
- List the three riskiest assumptions.
- State which parts cannot be used for build decisions.
- Include kill criteria.

## 3. Status Tags

Every factual claim carries a tag:

- `[Verified F-01]`: supported by evidence; include the source.
- `[Assumption A-01]`: plausible but unverified; include a test.
- `[Guess G-01]`: assistant inference; state that it may be wrong.
- `[Open Q-01]`: needs the user's answer.
- `[External source R-01]`: public source with URL and date.

Tags are not decoration. A factual claim without a tag is treated as unverified.

## 4. Assumption Register

The assumption register is a core artifact, not an appendix. Put it near the front of the decision memo or PRD.

| ID | Assumption | Risk | Current evidence | Test | Threshold | Status |
|---|---|---|---|---|---|---|
| A-01 | Users will pay to save 4 hours per week | High | E0 verbal interest | 5 pre-sales | ≥2 prepay | Unverified |
| A-02 | AI can reliably extract requirements from chat logs | High | None | 50-sample eval | Key-field accuracy ≥85% | Unverified |

Sort by risk × uncertainty × impact on the decision. Put the most dangerous assumption first.

## 5. L0 Decision Memo

Must include:

- Judgment: CONTINUE / NARROW / PIVOT / PAUSE / STOP.
- Confidence: high / medium / low.
- One-sentence reason.
- Target user and problem.
- Strongest evidence (with IDs).
- Biggest risk / strongest counter-case.
- Narrowest wedge (if continuing).
- Next cheapest validation.
- Kill criteria.
- What evidence would change the judgment.

Template: `outputs/decision-memo.md`.

## 6. L1 Lean PRD

Suggested 8–10 sections:

1. One-sentence summary.
2. Target user and problem.
3. Evidence and current alternatives.
4. Narrowest wedge and value proposition.
5. MVP scope and non-goals.
6. Core user journey.
7. Technology and AI approach (brief).
8. Metrics and success criteria.
9. Risks, assumptions, and validation plan.
10. Next step.

Do not add irrelevant sections to fill a template. Template: `outputs/lean-prd.md`.

## 7. L2 Full PRD

Use only when:

- The decision gate returns CONTINUE.
- The user needs it for fundraising, hiring, multi-team coordination, or formal review.
- The user explicitly asks for a full PRD.
- Key assumptions have at least E1/E2 evidence, or are clearly marked for validation.

### Section Selector

Do not mechanically write 25 sections. Choose by product type:

| Product type | Required sections | May omit |
|---|---|---|
| AI product | User/problem, evidence, wedge, AI role, inputs/outputs, quality and failure handling, data, evaluation, cost/latency, UX, stack, metrics, risks | Complex enterprise permissions (if consumer) |
| Marketplace | Supply/demand, trust, payments/escrow, disputes, matching, cold start, operations, risk | Complex AI (if irrelevant) |
| Internal tool | Workflow, roles/permissions, data boundaries, integrations, audit log, exception handling, adoption metrics | Consumer growth, brand |
| B2B SaaS | User/buyer/decision-maker, security, permissions, integrations, admin, pricing, procurement | Consumer social growth |
| Mobile app | Platform, entry point, notifications, offline, permissions, app-store review, retention loop | Complex enterprise admin |
| Regulated product | Licenses/filings, data compliance, content moderation, audit, human review, risk tiers | Premature growth detail |

Template: `outputs/full-prd.md`. The template is also trimmable, not a checklist.

## 8. L3 Build Spec

A spec for a coding agent or engineering team must include:

- Product goal and success criteria.
- User stories.
- Given/When/Then acceptance criteria.
- Data model: entities, fields, relationships, constraints.
- API/events: inputs, outputs, error codes, idempotency.
- Roles and permissions.
- Core state machine.
- Empty, loading, error, retry, and rollback states.
- AI inputs, outputs, eval set, failure handling, human confirmation.
- Non-functional requirements: performance, security, privacy, observability.
- Test plan.
- Phased delivery and rollback strategy.

Template: `outputs/build-spec.md`.

## 9. Evidence Appendix

L2/L3 may include an evidence appendix, but do not bury core judgments in it.

Appendix contents:

- Evidence ledger.
- Research sources.
- Interview summaries (redacted).
- Validation results.
- Remaining open questions.

## 10. Quality Check

Before output:

- Does the opening answer the user's question?
- Is there a decision, confidence, and reason?
- Is there an assumption register sorted by risk?
- Does every key fact have a tag?
- Are non-goals stated?
- Are kill criteria stated?
- Are confirmed facts, assistant inferences, recommendations, and open questions separated?
- Did you avoid complete-looking sections with no evidence?
- Can an engineer or designer start working from this?
- If the decision is PAUSE/STOP, did you avoid writing a full PRD?

## 11. Common Mistakes

- Writing 25 sections because the user said “PRD.”
- Writing assumptions as facts.
- Adding irrelevant sections for completeness.
- Listing features without failure states or permissions.
- Using vanity metrics that do not connect to user value.
- Omitting non-goals and letting scope expand.
- Omitting kill criteria, so the project cannot stop.
- Turning the decision memo into a summary of a PRD instead of an independent judgment.
