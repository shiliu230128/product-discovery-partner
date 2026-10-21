# Full PRD Template

A full PRD is conditional, not the default. Use it only when the decision gate is CONTINUE and the user needs it for fundraising, hiring, multi-team coordination, or formal review.

Read the section selector in `output-contract.md` first. Keep only relevant sections.

---

# [Product Name] PRD

Version: v0.1
Date: YYYY-MM-DD
Status: Draft / In review / Confirmed
Decision gate: CONTINUE
Confidence: High / Medium / Low

## 0. Decision Summary

- Judgment: CONTINUE
- One-sentence reason:
- Biggest risk:
- Strongest counter-case:
- Kill criteria:

## 1. Background and Opportunity

- Why this product is needed now:
- Why current solutions are insufficient:
- Opportunity window:
- Key external changes:

Mark `[Verified F-01]`, `[Assumption A-01]`, `[External source R-01]`.

## 2. Target Users and Personas

- First users:
- User / buyer / decision-maker / influencer:
- Current workflow:
- Pain frequency and severity:
- Success criteria and cost of failure:
- Where to find the first 20 users:

## 3. Problem Definition

- Trigger scenario:
- Current behavior:
- Cost of the pain:
- Consequence of not solving it:
- Why it is worth solving now:

## 4. Current Alternatives

| Alternative | Use case | Cost | Why it is insufficient |
|---|---|---|---|
| Manual work | ... | ... | ... |
| Excel/docs | ... | ... | ... |
| Competitor | ... | ... | ... |
| Tolerating it | ... | ... | ... |

## 5. Demand Evidence

- Strong evidence (E2/E3):
- Medium evidence (E1):
- Weak signals (E0):
- Evidence still missing:

## 6. Narrowest Wedge

- First users:
- Smallest testable result:
- Smallest deliverable form:
- Why this wedge fits v1:
- Explicit non-goals:

## 7. Core Value Proposition

- Core promise:
- First “worth it” moment:
- Behavior change:
- Advantage versus alternatives:
- What remains if a competitor copies 80%:

## 8. Goals and Non-Goals

### Goals

- What the MVP validates:
- What the user must complete:
- Business/learning goal:

### Non-Goals

- ...
- ...

## 9. MVP Scope

### P0

| Feature | User value | Why P0 | Acceptance criteria |
|---|---|---|---|
| ... | ... | ... | ... |

### P1

- ...

### P2 / Future

- ...

## 10. Core User Journey

1. Entry
2. Initial state
3. User input/selection
4. System processing
5. Result
6. Confirm/edit/share/export
7. Retention action

Failure paths and recovery:

- ...

## 11. Functional Requirements

For each feature:

- Feature name
- User story
- Trigger
- Main flow
- Edge cases
- Acceptance criteria

## 12. Non-Functional Requirements

- Performance
- Availability
- Security
- Privacy
- Compliance
- Scalability
- Observability
- Multi-platform behavior

## 13. UX Requirements

- First-run experience
- Empty states
- Loading states
- Error states
- Permission denied
- AI uncertainty/failure
- Trust and explainability
- Accessibility

## 14. Data Requirements

- Core objects
- Fields
- Data sources
- Permissions
- Lifecycle
- Import/export
- Redaction and deletion

## 15. AI / Model Requirements

If applicable:

- AI role
- Inputs/outputs
- Model capability requirements
- RAG / Agent / tool calling / multimodal
- Eval metrics and eval set
- Hallucination and error handling
- Human confirmation/rollback
- Cost and latency
- Data loop

## 16. Technical Stack Recommendation

```text
Recommended stack:
- Frontend:
- Backend:
- Database:
- Auth:
- AI / model layer:
- File / object storage:
- Payments:
- Notifications:
- Analytics:
- Deployment:
- Monitoring and logs:
- Admin tooling:

Why this fits:
- ...

Tradeoffs:
- ...

MVP shortcut:
- ...

When to switch:
- ...
```

## 17. System Architecture

- Main modules
- Data flow
- Third-party integrations
- Async jobs
- Permission boundaries
- Logs and auditability

## 18. Roles and Permissions

- User
- Admin
- Team member
- Reviewer
- External collaborator

## 19. Integrations

- Required integrations
- Optional integrations
- Webhook / API
- Import/export

## 20. Admin and Operations

Operators need to:

- View what
- Edit what
- Review what
- Handle which exceptions

## 21. Metrics

- North Star Metric
- Activation
- Retention
- Conversion/payment
- Quality
- Business
- Guardrail

For AI products, add:

- Accuracy
- Human correction rate
- Hallucination rate
- Average latency
- Cost per task

## 22. Edge Cases and Failure States

- No data
- Bad data
- Permission denied
- Integration failure
- AI failure
- User abandons
- Payment failure
- Duplicate submission
- Rollback/recovery

## 23. Premise Challenge and Alternatives

- 3–5 key premises
- Riskiest premise
- At least 2 alternative paths
- Recommended path and why
- User-confirmed vs open

## 24. Risks and Validation Plan

| Risk | Type | Impact | Test | Threshold | Status |
|---|---|---|---|---|---|
| ... | Product/technical/market/data/compliance | ... | ... | ... | ... |

## 25. Roadmap

- MVP
- V1
- V2
- Long-term direction

## 26. Product Recommendations

- Recommended wedge
- Scope to cut
- Key validation experiment
- Capability worth designing early
- Metric/assumption most likely to mislead

## 27. Open Questions

- [Q-01] ...

## 28. Evidence Appendix

- Evidence ledger
- Research sources
- Interview summaries (redacted)
- Validation results

## Quality Check

- [ ] Does every key judgment have a status tag?
- [ ] Are the strongest counter-case and kill criteria present?
- [ ] Are sections selected for the product type?
- [ ] Are facts, assumptions, guesses, and open questions separated?
- [ ] Are non-goals included?
- [ ] Can it directly support design, engineering, and review?
