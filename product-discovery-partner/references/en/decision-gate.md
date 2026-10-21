# Decision Gate

The decision gate is a core output of Product Discovery Partner. It prevents an output bias: no matter what the evidence says, the session ends with a PRD. Not every idea deserves build effort, and not every stage needs a document.

## 1. When to Run It

- After the problem, user, and evidence slots are covered, make an early call.
- Before MVP design, make a scope call.
- Before writing any PRD or build spec, make a formal decision.
- When the user asks “is this worth doing?” or “should we continue?”
- After the user writes back validation results.

## 2. Six Dimensions

Score each dimension 0–2. The score is for exposing disagreement, not for manufacturing certainty.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Problem evidence | Only E0 verbal interest | E1/E2, but small sample or narrow scenario | E3 or multiple independent E2 sources; frequency and cost are clear |
| User reachability | No idea where to find users | A channel exists but is unverified | Can list the first 20 target users and reach them |
| Wedge testability | Too broad to test soon | Testable, but expensive | A minimum test is possible in 2–4 weeks |
| Technical feasibility | Core capability is impossible or unaffordable | Feasible with meaningful risk | Mature options; risk and cost are manageable |
| Business loop | No idea who pays | A hypothesis exists, unverified | Payment evidence or a clear path to payment |
| Risk | Unacceptable safety, compliance, or ethical risk | Risk exists but can be mitigated | Risk is understood with fallbacks |

The total is not the only input. Any 0 can trigger PAUSE or STOP, especially in problem evidence, reachability, and risk.

## 3. Five Outcomes

### CONTINUE

Conditions:

- The problem is real, frequent, and costly enough.
- The first users are specific and reachable.
- The wedge can be tested in 2–4 weeks.
- Technical, business, and risk dimensions have no fatal issue.

Output: move to the artifact stage. Choose lean PRD, full PRD, or build spec based on the user's need.

### NARROW

Conditions:

- The direction is broadly viable, but the user, scenario, or workflow is too broad.
- Resources cannot serve multiple segments at once.

Output: narrow to one user segment and one closed-loop workflow. Rewrite the MVP and non-goals.

```text
The issue is not “not enough features.” It is “too many users.” I recommend serving only [specific segment] with [specific workflow] first, and explicitly listing other scenarios as non-goals.
```

### PIVOT

Conditions:

- One core judgment about the user, problem, value proposition, or business model is wrong.
- Continuing costs more than changing the wedge.

Output: give two alternative paths, explain fit, cost, and risk, and recommend one.

### PAUSE

Conditions:

- Key evidence is insufficient to decide CONTINUE or STOP.
- The cheapest next step is validation, not development.

Output: decision memo + validation pack. State clearly why a full PRD is not appropriate yet.

```text
The biggest issue is not feature design. It is that we do not know whether users will pay for this result. Writing a PRD now would freeze an unverified assumption. Run 5 user interviews and one pre-sale test first.
```

### STOP

Conditions:

- The problem is not painful or frequent enough.
- The current workaround is good enough; users have no reason to switch.
- Target users are unreachable or acquisition is too expensive.
- Unit economics do not work.
- There is an unacceptable safety, compliance, or ethical risk.

Output: decision memo with the reason, strongest counter-case, and what evidence would change the judgment. Do not write a PRD.

```text
My judgment is that this product should not be built now. The strongest evidence is verbal interest; the current workaround costs less than one hour per month; and the target users cannot be reached without violating platform rules. If you can get three paying users or one mandatory use case, my judgment would change.
```

## 4. What Every Decision Must State

- **Judgment:** CONTINUE / NARROW / PIVOT / PAUSE / STOP.
- **Confidence:** high / medium / low.
- **Reason:** 3–5 points with evidence IDs.
- **Strongest counter-case:** what would most likely make this judgment wrong.
- **What would change the judgment:** specific evidence or threshold.
- **Kill criteria:** what result triggers a stop or pivot.
- **Next step:** the cheapest, fastest action that reduces the biggest risk.

## 5. Kill Criteria

Kill criteria must be written before development, not explained after failure.

Good kill criteria:

- Fewer than 3 of 30 qualified users complete the core action within two weeks.
- Fewer than 4 of 10 interviewees can describe a specific problem that happened in the past month.
- Fewer than 2 of 20 qualified users are willing to prepay or put down a deposit.
- AI accuracy on key fields is below 85% on a 50-sample eval set.
- Customer acquisition cost stays above one-third of average revenue for 30 days.
- An unacceptable compliance, safety, or content risk appears.

Bad kill criteria:

- “Users did not like it” (not observable).
- “Growth is too slow” (no baseline).
- “It feels wrong” (not reproducible).

## 6. Pre-mortem

Before CONTINUE, run a quick pre-mortem:

```text
Assume this product failed six months from now. What are the three most likely reasons?
1.
2.
3.

Which reason is most likely during the MVP stage? Can we test it within two weeks?
```

The goal is not to scare the user. It is to turn the biggest failure mode into a validation task.

## 7. Anti-Sycophancy Check

Before deciding, ask yourself:

- Am I avoiding STOP because the user has invested a lot of time?
- Am I treating excitement as evidence?
- Am I producing a complete-looking PRD that avoids “should this exist?”
- Did I write the strongest counter-case?
- If this were my money, would I keep investing?

If the answer is uncertain, lower the confidence. Do not raise the volume.

## 8. Decision Memo Template

```markdown
# Decision Memo: [Product Name]

## Judgment
CONTINUE / NARROW / PIVOT / PAUSE / STOP
Confidence: high / medium / low

## One-sentence reason
...

## Current evidence
- [F-01] ...
- [A-01] ...

## Strongest counter-case
...

## What would change the judgment
...

## Next step
...

## Kill Criteria
...
```

## 9. Common Mistakes

- Turning the gate into a scoring game and ignoring fatal risk.
- Scoring every dimension 1 and defaulting to CONTINUE.
- Being unable to say STOP because the user has invested effort.
- Calling PAUSE “build the MVP first,” which skips validation.
- Writing no kill criteria, so the project cannot stop.
- Listing only evidence that supports the current direction.

The value of the decision gate is not a beautiful score. It is making “do not build,” “not yet,” and “change direction” legitimate outputs.
