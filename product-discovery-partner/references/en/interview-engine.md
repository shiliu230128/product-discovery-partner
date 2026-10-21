# Interview Engine

This file defines how Product Discovery Partner chooses the next question, when to jump, and how to checkpoint and resume. The goal is not to finish ten stages. The goal is to reduce the biggest uncertainty with the fewest questions.

## 1. Depth Modes

| Mode | Question budget | Use when | Default artifact | What it cannot promise |
|---|---|---|---|---|
| Quick | About 8 questions | Early judgment, internal discussion, deciding whether the idea is worth pursuing | Decision memo + 3 key assumptions + next validation | A validated PRD |
| Standard | 15–20 questions | Preparing an MVP, aligning a small team | Lean PRD + validation pack | Full technical detail |
| Deep | 30+ adaptive questions | Fundraising, hiring, high-risk or complex products | Full PRD + build spec + AI eval set | A substitute for real user research or legal advice |

### Session Start Script

```text
Let me confirm the direction I understand: you want to build [one-sentence restatement].

I recommend the [mode] for this session:
- Quick: about 8 questions, ending with a one-page decision memo instead of a full PRD.
- Standard: about 15–20 questions, ending with a lean PRD and validation pack.
- Deep: 30+ questions, ending with a full PRD and build spec.

I recommend [mode] because [reason]. Does that work?
```

Do not turn this into a long questionnaire. If the user already says “quick check” or “full PRD,” confirm in one sentence and begin.

## 2. Eight Slots

Each slot has a status: `empty / provisional / confirmed / overturned / needs evidence`.

### Slot 1: Problem and Trigger

Answer:

- What specific moment made the user think of this product?
- How often does the problem happen?
- What is lost if it is not solved: time, money, revenue, risk, emotion, coordination cost?
- Is this based on real observation, personal pain, a customer request, or a technical possibility?

Completion bar: one concrete scene with frequency and at least one cost.

Common failure: abstract descriptions such as “inefficient” or “scattered information” with no moment or consequence.

### Slot 2: User and Buyer

Answer:

- Who uses it, who pays, and who decides?
- Who feels the pain most urgently? Why would they try an imperfect version now?
- Where can you find the first ten users?
- What are the user's role, goals, pressure, budget, and cost of failure?

Completion bar: a specific user segment and at least one reachable channel.

Common failure: “SMBs,” “product managers,” or “creators” are still too broad.

### Slot 3: Evidence and Current Workaround

Answer:

- What does the user do today: manual work, spreadsheets, chat, documents, competitors, outsourcing, or tolerating the problem?
- What are the time, money, error, and coordination costs of the current approach?
- What is the strongest evidence: behavior, artifact, payment, workflow dependency, or verbal interest?
- Who would be genuinely upset if this product disappeared tomorrow?

Completion bar: at least one E2 evidence item, or an explicit evidence gap and next validation step.

Common failure: treating “friends like it” or a waitlist as strong demand.

### Slot 4: Value and Wedge

Answer:

- What is the first moment the user feels the product is worth it?
- What is the smallest deliverable result: a report, an action, an insight, an export?
- Why now? What changed in technology, policy, platforms, or user behavior?
- If a competitor copied 80% of the features, what advantage remains?

Completion bar: the wedge closes a loop for one specific user segment and can be explained in one sentence.

Common failure: value claims such as “more convenient,” “smarter,” or “all-in-one platform.”

### Slot 5: Flow and Experience

Answer:

- Where does the user enter? What do they see first?
- What steps complete the core task?
- Where are they most likely to abandon or lose trust?
- How do empty, loading, error, permission-denied, and recovery states work?
- Are notifications, collaboration, history, or export needed?

Completion bar: a main path and at least two failure paths.

Common failure: listing features without describing user states or failure recovery.

### Slot 6: MVP and Non-Goals

Answer:

- If you could build only three features to validate value, which three?
- What will v1 explicitly not do?
- What is the success bar: completing the core action, repeated use, payment, or a business outcome?
- Can you validate with manual work, a semi-automated process, no-code tools, or an existing API?
- What is the smallest version someone would pay for, reuse, or depend on?

Completion bar: scope can be validated in 2–4 weeks and non-goals are explicit.

Common failure: the MVP is a smaller copy of the full product instead of a testable value loop.

### Slot 7: Technology and AI

Answer:

- Target platform: web, mobile, mini program, desktop, extension, bot, or API-first?
- What does the team know best? What are the budget, launch date, and expected scale?
- Is AI necessary? Is it the core value or an efficiency layer?
- Where does data come from? Who can access it? Are real-time collaboration, payments, notifications, admin, integrations, or compliance needed?
- What happens if AI is wrong? Are citations, confidence, human review, or rollback needed?
- Which technical decisions are irreversible?

Completion bar: platform, data, AI role, and irreversible decisions are clear.

Common failure: recommending complexity for its own sake, or leaving AI failure handling undefined.

### Slot 8: Business, Metrics, and Decision

Answer:

- Who pays, why, and with what pricing model?
- Where do the first 100 users come from?
- Does retention come from data, collaboration, habit, content, or business results?
- Which three metrics matter most after 30 days?
- Which metric could look good without proving value?
- What is the biggest failure assumption? What are the kill criteria?

Completion bar: a clear CONTINUE / NARROW / PIVOT / PAUSE / STOP judgment is possible.

Common failure: revenue goals without a retention mechanism or kill criteria.

## 3. Choosing the Next Question

Each turn:

1. **Check overturned slots first.** If the user just changed an upstream assumption, revisit the most affected downstream slot.
2. **Then look for empty, high-risk slots.** Problem, user, and evidence come before tech stack and business model.
3. **Within a slot, ask the question most likely to falsify the current judgment.** Not “tell me more,” but “what answer would make this direction wrong?”
4. **If the user is fatigued or near the budget,** stop and produce the best artifact the current evidence supports. Mark high-risk assumptions.
5. **If the user explicitly asks about a topic,** jump there, but record unfinished slots.

A rough priority formula:

```text
risk × uncertainty × impact on the decision
```

Do not ask questions whose answer is already obvious. Do not use question count to perform expertise.

## 4. Handling Vagueness, Missing Information, and Contradictions

### Vague Answers

Do not repeat the same question. Offer 2–3 possible directions, explain when each fits, give a recommendation, and let the user choose or correct you. Then continue.

```text
“Improve efficiency” is still too broad. Here are three possible wedges:
A. Turn meeting notes into action items.
B. Cluster scattered customer feedback into product insights.
C. Help new employees find internal answers faster.

I recommend B because it connects directly to product decisions and is easier to prove valuable. You can correct me.
Next question: what specific moment made you think of this product?
```

### User Cannot Answer

Mark it `[Open Q-01]`, give a provisional assumption `[Assumption A-01]`, and move to the next high-value slot. Do not get stuck.

### Contradictions

Name the contradiction directly:

```text
Earlier you said the first users are product managers, but just now you said the main users are salespeople. Those two groups have different pain and buying reasons. Let's settle this first: who is the first paying user?
```

### New Evidence Overturns an Old Conclusion

Mark affected conclusions `stale`, explain why they need review, and ask the single question with the largest impact.

## 5. Jump, Backfill, Checkpoint, Resume

### Jump

If the user says “let's talk about the tech stack,” “jump to the business model,” or “skip to the MVP,” jump there. Keep unfinished slots in the state block.

```text
Sure. I'll note that the user and evidence slots are still open, and jump to the tech stack. If we write a PRD later, I'll come back to close those gaps.
```

### Backfill / Correction

When the user adds new information or changes their mind:

1. Update the evidence ledger.
2. Mark affected downstream slots `stale`.
3. Explain the impact in one sentence.
4. Ask the single most important follow-up.

### Checkpoint

Emit a state block at natural checkpoints: after problem/user/evidence, after the MVP, and before the decision gate. Do not emit it every turn.

```markdown
## Discovery State
- depth: standard
- turn: 12/18
- confirmed: [F-01] Target users are product leads at 10–50 person B2B SaaS teams; [F-02] They spend about 4 hours per week manually organizing feedback
- assumptions: [A-01] Teams will pay to save those 4 hours (risk: high, test: 5 pre-sales)
- open: [Q-01] Who makes the final purchase decision
- stale: none
- next: Confirm the buyer and budget
```

If the environment supports file writes, save it as `discovery-state.md`; otherwise ask the user to copy it.

### Resume

When the user pastes a state block or says “continue,” first restate:

- current mode and progress
- 2–3 confirmed facts
- the biggest 1–2 assumptions
- the next question

Then continue. Do not restart from the beginning.

## 6. Question Budget and Fatigue

- Quick: about 8 questions. Standard: 15–20. Deep: 30+.
- At 70% of the budget, pause:

```text
We've asked about [N] questions and covered [slots]. The remaining gaps are [gaps].
You can continue, drop to a lower depth and use what we have, or stop here.
```

- If the user says “I'm tired,” “let's stop,” or “just give me the conclusion,” do not push through. Produce the best artifact the current evidence supports and mark high-risk assumptions.
- At the end of quick mode, state clearly: this is triage, not a validated PRD.

## 7. Ending the Interview

An interview can end for three reasons:

1. **Enough information:** run the decision gate, then produce the artifact defined by the output contract.
2. **Budget exhausted:** produce the best current artifact and mark gaps and high-risk assumptions.
3. **User asks to stop:** respect it, but do not pretend the information is complete. Explain which judgments cannot yet be made.

Before ending, summarize:

```text
Let me sync what is currently locked:
1. ...
2. ...

The biggest unvalidated assumption is:
- ...

I recommend [decision gate / validation pack / decision memo / lean PRD] next.
```

Do not automatically write a full PRD without confirmation. State which output tier you plan to produce and why.
