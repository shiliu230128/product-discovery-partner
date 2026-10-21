# Build Spec Template

Use when handing work to a coding agent or engineering team. A build spec is not a restatement of the PRD; it is a specification that can become tasks and tests directly.

---

# [Product/Module Name] Build Spec

Version: v0.1
Date: YYYY-MM-DD
Upstream PRD:
Decision gate: CONTINUE

## 1. Goal and Success Criteria

- User outcome to deliver:
- Out of scope:
- Success criteria:
- Kill criteria:

## 2. User Stories

```text
As a [role],
I want [action],
so that [outcome].
```

For each story:

- Priority: P0/P1/P2
- Dependencies:
- Evidence/assumption:

## 3. Acceptance Criteria

Use Given/When/Then:

```text
Given [initial state]
When [user action/system event]
Then [observable result]
```

Cover:

- Main path
- Empty state
- Error state
- Permission denied
- Retry/recovery
- Boundary values

## 4. Data Model

### Entities

| Entity | Field | Type | Required | Constraint | Notes |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

### Relationships

- ...

### Indexes and Unique Constraints

- ...

### Data Lifecycle

- Create:
- Update:
- Delete/archive:
- Export:
- Redaction:

## 5. API / Events

| Method | Path/Event | Input | Output | Error Code | Idempotent |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Additional:

- Auth
- Rate limits
- Timeouts
- Retry policy
- Webhook signatures
- Version compatibility

## 6. Permissions and Roles

| Role | View | Create | Edit | Delete | Export |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

Specify:

- Tenant/team isolation
- Admin permissions
- Audit log
- Sensitive-field access

## 7. Core State Machine

```text
[State A] --event--> [State B] --event--> [State C]
```

List:

- Valid states
- Invalid transitions
- Failure/retry
- Human intervention
- Timeout/cancel

## 8. Frontend/UX Specification

- Pages/entry points
- Components
- Empty states
- Loading states
- Error states
- Permission denied
- Mobile/desktop behavior
- Accessibility

## 9. AI Specification (If Applicable)

- Inputs:
- Output schema:
- Model/provider:
- Prompt/workflow:
- Tool-calling boundaries:
- Human confirmation points:
- Failure handling:
- Eval set:
- Quality thresholds:
- Latency/cost limits:
- Logging and observability:

## 10. Non-Functional Requirements

- Performance:
- Availability:
- Security:
- Privacy:
- Compliance:
- Observability:
- Backup/recovery:

## 11. Test Plan

### Unit Tests

- ...

### Integration Tests

- ...

### E2E

- ...

### AI Evaluation

- Sample size:
- Metrics:
- Pass threshold:
- Regression mechanism:

### Manual Acceptance

- ...

## 12. Delivery and Rollback

- Milestones:
- Rollout/feature flags:
- Data migration:
- Rollback steps:
- Monitoring and alerts:
- Owners:

## 13. Open Questions

- [Q-01] ...

## Quality Check

- [ ] Does every P0 user story have acceptance criteria?
- [ ] Does the data model include constraints and lifecycle?
- [ ] Are permissions and tenant isolation defined?
- [ ] Are failure, retry, and rollback covered?
- [ ] Does AI have an eval set and failure handling?
- [ ] Can an engineer break this into tasks directly?
