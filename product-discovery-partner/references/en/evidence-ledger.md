# Evidence Ledger

The evidence ledger is what separates Product Discovery Partner from an interview chatbot. It prevents a common failure: the user answers from memory, the assistant turns that memory into a fact, and the final PRD looks complete while resting on little evidence.

## 1. Evidence Levels

| Level | Name | Examples | What it can support |
|---|---|---|---|
| E0 | Weak signal | “That sounds interesting,” friends' support, a waitlist, generic “there is demand” | Only “worth exploring further” |
| E1 | Specific statement | A user describes the last time they hit the problem, a direct quote, one real scenario | Forming a hypothesis, not proving broad demand |
| E2 | Behavioral trace | Screenshots, spreadsheets, tickets, chat logs, a repeated workaround, real time or data invested, multiple independent users | Moving into MVP design and validation |
| E3 | Strong commitment | Payment, prepayment, signed contract, production dependency, observable behavior at scale | Continued investment, subject to retention and scale checks |

E0 cannot be promoted to “validated.” E1 needs multiple independent sources before it becomes a pattern. E2 and E3 still need source, date, and scope; they cannot be extrapolated indefinitely.

## 2. Ledger Structure

Maintain at least these fields. Use a Markdown table, or a file such as `evidence-ledger.md` or JSON when the environment supports it.

| ID | Claim / fact | Type | Source | Level | Status | Confidence | Linked decision |
|---|---|---|---|---|---|---|---|
| F-01 | Target users are product leads at 10–50 person B2B SaaS teams | Fact | User interview, 2026-10-12 | E1 | Provisional | Medium | User selection |
| A-01 | Teams will pay to save 4 hours per week | Assumption | User inference | E0 | Unverified | Low | Business model |
| G-01 | No competitor covers the Feishu workflow | Guess | Assistant inference | E0 | Unverified | Low | Differentiation |
| Q-01 | Who makes the final purchase decision | Open | Not asked yet | — | Open | — | Buyer |
| R-01 | Competitor X charges 99 RMB per seat per month | External fact | Pricing page, 2026-10-12 | E2 | Verified | Medium | Pricing |

### Types

- `Fact`: explicitly confirmed by the user or supported by a reliable source.
- `Assumption`: reasonable but unverified.
- `Guess`: assistant inference with weak evidence.
- `Open`: a question that needs an answer.
- `External fact`: a finding from a public source.

### Status

- `Unverified`
- `Provisional`
- `Verified`
- `Overturned`
- `Expired` (the environment changed; recheck)

### Confidence

- `Low`: only E0 or one informal source.
- `Medium`: E1/E2 evidence, but a small sample or narrow scenario.
- `High`: E3 or multiple independent E2 sources directly relevant to the decision.

## 3. Citation Rules in Outputs

Every factual claim carries a tag:

- `[Verified F-01]`: supported by evidence; include the source.
- `[Assumption A-01]`: plausible but unverified; include a test.
- `[Guess G-01]`: assistant inference; state that it may be wrong.
- `[Open Q-01]`: needs the user's answer.
- `[External source R-01]`: public source with URL and date.

Rules:

- Numbers, user quotes, competitor capabilities, prices, and regulatory requirements without a source cannot be written as facts.
- When the user says “many users” or “everyone thinks,” ask for count, sample, and source. If unavailable, mark E0.
- Do not disguise assistant recommendations as user-confirmed facts.
- Do not remove unfavorable evidence. Put it in “strongest counter-case” or “risks.”

## 4. Source Rules

### User Sources

- Prefer “when did this last happen?” over “what do you usually do?”
- Ask for a concrete artifact: screenshot, spreadsheet, ticket, chat log, quote, meeting note. Request only the minimum needed for the decision.
- Record the user's own words, not only your summary.
- Distinguish user, buyer, decision-maker, and influencer.

### External Sources

Source priority:

1. Primary data: official docs, pricing pages, regulatory text, public filings, the actual product.
2. Independent secondary sources: credible media, industry reports, academic research.
3. Vendor marketing: proves what the vendor claims, not what works.
4. Assistant memory: not a source. If the user needs current information, say it must be verified online.

For each external item, record the source name, URL, access date, summary, and scope.

### Research Downgrade

When web access is unavailable:

- Say clearly: “I cannot verify this online right now.”
- Provide exact search queries and a fill-in table.
- Do not invent competitors, prices, funding, regulations, or model capabilities.
- Mark user-provided external information as `[External source R-xx]` and note “provided by user, not independently verified.”

## 5. Contradictions and New Evidence

When new information conflicts with an old conclusion:

1. Name the conflict; do not silently overwrite.
2. Find affected conclusions and downstream decisions.
3. Mark affected items `stale`.
4. Ask one question that resolves the conflict.
5. Update the ledger and artifacts.

Example:

```text
Earlier you said the buyer is the product lead, but just now you said IT approves the purchase. That changes the value proposition and pricing.
I'm marking “buyer” as open. First question: who signed for similar tools in the past?
```

## 6. Writing Back Validation Results

When the user completes a test, collect:

```text
Test type:
Sample:
What actually happened:
Quotes / artifacts:
Key numbers:
Surprises:
```

Then:

- Convert results into evidence entries with level and source.
- Update the relevant assumptions' status and confidence.
- If results are ambiguous, say “this is not enough to continue.” Do not rationalize.
- Produce a new decision memo: continue, narrow, pivot, pause, or stop.

## 7. Privacy and Redaction

- Collect only the minimum data needed for the decision.
- Get consent before recording interviews, chat logs, or customer lists.
- Remove names, companies, contact details, order numbers, and identifying information from examples, demos, and external artifacts.
- Do not send sensitive user data to an external service unless the user explicitly agrees and the environment allows it.
- For personal data, medical, financial, children's data, or similar sensitive domains, raise consent and compliance questions early.

## 8. Common Mistakes

- Treating “willing to try” as “willing to pay.”
- Treating waitlist size as demand strength.
- Accepting “often” without asking for frequency.
- Treating vendor marketing as independent evidence.
- Writing assistant inferences as “the user said.”
- Recording only evidence that supports the current direction.
- Keeping evidence in an appendix that does not affect the decision.

The purpose of the ledger is not to make documents heavier. It is to make every important judgment challengeable. If a judgment cannot be supported, downgrade it to an assumption and design a cheap test.
