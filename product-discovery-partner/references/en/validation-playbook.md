# Validation Playbook

Validation is not “go talk to users.” Validation means writing a falsifiable assumption, designing a test that produces a clear signal within a limited time, and using the result to change a decision.

## 1. When to Use It

- The user has only verbal interest and no behavioral evidence.
- It is unclear how users solve the problem today or what it costs.
- It is unclear whether users will pay or change their workflow.
- There is no evidence that AI quality is sufficient or trusted.
- The decision gate returns PAUSE and the cheapest next step is validation.
- The team is about to build, but the biggest assumption is still untested.

Do not run a generic “user interview” when the assumption is unclear. Pick the assumption most likely to overturn the current direction.

## 2. Choose the Riskiest Assumption

Sort by “if this is wrong, which decision changes?” not by ease of testing.

Typical priority:

1. Is the problem real, frequent, and costly enough?
2. Will users change their current behavior?
3. Will users pay or invest real data?
4. Does the solution produce a result users value?
5. Does AI/technical quality reach the usable threshold?
6. Do acquisition and retention work?

Write it as a falsifiable sentence:

```text
We believe [specific user] in [specific scenario] will [specific behavior] because [specific cost/motivation].
If this is wrong, we should [which decision changes].
```

## 3. Test Types

| Test | Question it answers | Stage | Main risk |
|---|---|---|---|
| Problem interview | Is the problem real, frequent, and costly? | Earliest | What users say differs from what they do |
| Artifact request | Will users show their real workflow and data? | Early | Privacy and sample bias |
| Fake door | Will users act on a specific value proposition? | Early | Deception and ethics |
| Concierge | Is a manually delivered result valuable? | Early | Hard to scale |
| Pre-sale / deposit | Will users pay? | Middle | Refunds, commitments, compliance |
| Pricing test | Price sensitivity and packaging | Middle | Stated price is not a real purchase |
| Workflow pilot | Will users connect their workflow? | Middle | Integration and switching cost |
| AI eval | Quality, latency, cost, hallucination | Middle | Sample may not represent real distribution |
| Retention test | Will users come back? | Later | Requires time and real users |

## 4. Validation Pack Template

```markdown
# Validation Pack: [Assumption Name]

## Assumption to test
We believe ...

## If wrong, what changes
...

## Test design
- Type:
- Sample:
- Recruitment:
- Duration:
- Cost:

## Script / assets
...

## Pass threshold
- Pass:
- Fail:
- Ambiguous:

## What each result triggers
- Pass -> CONTINUE / next stage
- Fail -> PIVOT / STOP
- Ambiguous -> increase sample or change test

## Ethics and privacy
- Is the test purpose disclosed:
- Is real payment involved:
- Is sensitive data collected:
- How is data redacted:
```

## 5. Problem Interview Guide

Goal: reconstruct past behavior. Do not pitch the idea.

### Recruitment Criteria

- Has experienced the problem in the last 1–3 months.
- Is a user, buyer, or decision-maker.
- Is not a friend, colleague, or someone helping out of politeness.

### Opening

```text
I'm researching [problem area], not selling a product. I'd like to hear about the last time you ran into this problem.
There are no right answers; specifics are more useful than generalizations. May I record this? If not, I'll take notes.
```

### Core Questions

1. When did this problem last happen? What exactly happened?
2. What did you do? Which tools and people were involved?
3. How much time, money, or other cost did it take?
4. Which step was most painful or error-prone?
5. Have you actively looked for a solution? What did you try, and why did you stop?
6. If this problem disappeared tomorrow, what would change? If it continues, what do you lose?
7. Have you paid for a similar problem before? Who paid, and how much?
8. Who else is affected? Who decides whether to adopt a new solution?

### Avoid

- “Would you use this product?” (hypothetical)
- “What do you think of this idea?” (politeness bias)
- “Would you pay if this feature existed?” (no real cost)
- Explaining your solution and watching for polite nodding.

### Closing

```text
If you're comfortable, could you show me one spreadsheet, screenshot, or workflow you mentioned?
If not, no problem. If I build a small prototype later, would you try it with your real data?
```

## 6. Fake Door Test

Goal: test whether users take action on a specific value proposition, not just express interest.

### Minimum Assets

- One-sentence value proposition.
- 3–5 specific benefits.
- A clear CTA: book a call, leave an email, request access, place a deposit.
- Price or price range if payment is a core assumption.
- A clear “coming soon / waitlist” disclosure.

### Metrics

- Visit → CTA click rate.
- CTA → signup/booking completion.
- Signup → actual attendance/reply rate.
- If prepayment is involved: payment conversion and refund rate.

### Ethics

- Do not pretend the product is already live.
- Do not collect non-refundable fees.
- Clearly state that this is a waitlist or research project.
- Do not fabricate testimonials, media endorsements, or customer logos.
- Follow platform advertising and privacy rules.

A fake door is not deception. It tests interest with real action while telling users the current status.

## 7. Concierge Test

Goal: deliver a complete result manually before writing software, to validate whether users value the outcome.

Steps:

1. Recruit 3–5 target users.
2. Ask them for real input.
3. Manually do the work the product would do.
4. Deliver the result within the promised time.
5. Observe whether users use, edit, share, request again, or pay.
6. Record how long it took, which step was hardest, and which judgments needed user confirmation.

Pass signals:

- Users actively use the result, not just thank you politely.
- Users provide more real data.
- Users pay or prepay for the next delivery.
- Users bring the result into a real decision.

Fail signals:

- Users say “nice” but do not use it.
- Users only try it when it is free and low-effort.
- You cannot deliver acceptable quality in a reasonable time.

## 8. Pre-Sale and Pricing Tests

- State the deliverable, timeline, and refund policy.
- Do not replace real payment with a vague “intent deposit.”
- Record who pays, why, whether they use it, and whether they refund.
- Test at least 2–3 price points; observe conversion and reaction, not just “is it expensive?”
- Early high-ticket service fees may validate value better than low-price subscriptions.

## 9. AI Eval Test

Build a small eval set before asking users to trust AI:

- 20–50 real or anonymized samples.
- Define key fields and pass criteria.
- Record accuracy, recall, human correction rate, hallucination rate, latency, and cost per task.
- Have target users judge whether the result is usable, not only the technical team.
- Keep failure samples as regression tests.

If AI errors cause high losses, default to “suggestion → human confirmation → execution,” not full automation.

## 10. Writing Back Results

After the test, collect:

```text
Test type:
Sample size and recruitment:
What actually happened:
Quotes / artifacts:
Key numbers:
Surprises:
```

Then update the evidence ledger:

- Convert results into E1/E2/E3 evidence.
- Update assumption status and confidence.
- If results are ambiguous, say “not enough to continue.”
- Produce a new decision memo.

Do not reinterpret ambiguous results as support just because the user has invested time.

## 11. Common Mistakes

- Deciding what to build first, then designing a test that must pass.
- Interviewing only friends and colleagues.
- Asking hypothetical questions instead of about past behavior.
- Treating “willing to try” as “willing to pay.”
- Having no pass/fail threshold.
- Not updating the decision after the test.
- Using a fake door to collect non-refundable fees or misrepresent product status.
- Extrapolating one interview to the whole market.

The purpose of validation is not to prove you are right. It is to find out quickly where you are wrong.
