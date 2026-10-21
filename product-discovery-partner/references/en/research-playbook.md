# External Research Playbook

User self-report is not enough for every judgment. Competitors, substitutes, pricing, channels, regulation, and technical capability often need external input. The goal is not to write an industry report. The goal is to answer questions that change the decision.

## 1. When to Research

- The user says “there are no competitors” or “we are first,” but is not sure.
- You need to judge substitutes, pricing, channels, or market saturation.
- The product involves regulation, licensing, data, content moderation, or platform rules.
- You need to assess AI models, APIs, cost, or latency.
- The user's market judgment is impressionistic and has no source.
- The decision gate needs external evidence to choose CONTINUE / PIVOT / STOP.

Do not run large-scale market research early. First ask: which external fact is most likely to change the current decision?

## 2. Research Questions

### Competitors and Substitutes

- Who are the direct competitors? Who do they serve, and what problem do they solve?
- What are the indirect substitutes: spreadsheets, manual work, outsourcing, internal systems, chat?
- Why do users choose the status quo over competitors?
- What are competitors' pricing, packaging, acquisition channels, and retention mechanisms?
- Does an existing product already cover 70% of the need? If so, what is the differentiation?

### Market and Users

- Where do target users gather: channels, communities, platforms, industries?
- Is the market growing, stable, or shrinking?
- Has a recent policy, technology, or platform change created an opening?
- What keywords do users search for today?

### Regulation and Compliance

- Are licenses, filings, approvals, or industry permits required?
- Does it involve personal data, payments, healthcare, finance, education, children, or content?
- Do platform rules restrict acquisition, automation, or data use?
- Can data be transferred across borders?

### Technology

- Do mature APIs or open-source options exist for the core capability?
- Do cost, latency, accuracy, and reliability meet product requirements?
- Is self-hosting, fine-tuning, or private deployment required?
- What are vendor lock-in and migration costs?

## 3. Source Levels

| Level | Source | What it can support |
|---|---|---|
| A | Official docs, pricing pages, regulatory text, public filings, the actual product | Factual judgments |
| B | Independent media, industry reports, academic research, credible databases | Trends and context |
| C | Vendor blogs, sales material, case studies | What the vendor claims, not proven effect |
| D | Assistant memory, unsourced summaries | Not evidence |

Rules:

- Record source name, URL, access date, and a short quote.
- Separate “fact” from “vendor claim.”
- Do not use one source to prove an entire market.
- Prices, funding, regulations, and model capabilities change; always date them.
- If you cannot verify it, mark `[Guess G-xx]` or `[Open Q-xx]`.

## 4. Online Research Protocol

If web search or fetch is available:

1. Write 3–5 specific research questions.
2. Run 1–2 targeted searches per question. Do not browse aimlessly.
3. Prefer primary sources.
4. Record URL, date, and key quotes.
5. Compress findings into “conclusion + evidence + impact on the decision.”
6. Add external evidence to the ledger with `[R-01]` IDs.

Output format:

```markdown
## Research Conclusions
- Conclusion 1: [one sentence]
  - Source: [name](URL), accessed YYYY-MM-DD
  - Confidence: high/medium/low
  - Impact on decision: ...

## Still Uncertain
- ...
```

Do not output a research log longer than the conclusions. The user needs judgment, not search history.

## 5. When Web Access Is Unavailable

State the limitation clearly:

```text
I cannot verify competitors and pricing online right now. I can give you a precise search checklist and a fill-in table. Paste the results back, and I'll update the judgment.
```

Provide:

- Exact search queries.
- Page types to check (pricing pages, app stores, regulatory text, job posts, etc.).
- A fill-in table: source, URL, date, key fact, impact on decision.
- Do not invent URLs, prices, funding, or regulatory clauses.

## 6. Competitor Scan Template

```markdown
# Competitor and Substitute Scan

## Target Users
...

## Direct Competitors
| Product | Target user | Core value | Pricing | Channel | Strengths | Weaknesses | Source |
|---|---|---|---|---|---|---|---|

## Indirect Substitutes
| Substitute | Why users use it | Cost | Why it may be insufficient |
|---|---|---|---|

## Current User Workflow
...

## Differentiation Hypothesis
- We believe ...
- Needs validation ...

## Impact on Decision
- CONTINUE / NARROW / PIVOT / PAUSE / STOP
```

## 7. Regulation and Platform Scan Template

```markdown
# Regulation and Platform Constraints

## Applicable Regions
...

## Required Licenses / Filings
- [ ] ...
- Source:
- Processing time:
- Cost:

## Data and Privacy
- What data is collected:
- Is consent required:
- Is cross-border transfer allowed:
- Retention period:

## Content and Platform Rules
- Platform:
- Restrictions:
- Review requirements:

## Impact on Product Scope
- MVP must include:
- Must defer:
- May be impossible:
```

For legal, medical, financial, children's, or other high-risk domains, state that this is not legal advice and recommend consulting a professional and checking the latest official requirements.

## 8. Research Theater

Avoid:

- Collecting many links without changing any judgment.
- Looking only for evidence that supports the current direction.
- Using a market-size report to prove demand instead of user behavior.
- Treating a competitor's feature list as user demand.
- Using “no competitors” as proof of opportunity without checking substitutes.
- Citing dead URLs or outdated data.

Every research item should answer: which judgment did it change? If none, leave it out of the artifact.

## 9. Writing Into the Evidence Ledger

After research:

- Create an `[R-xx]` entry for each key fact.
- Record source level, date, confidence, and scope.
- Flag conflicts with user self-report.
- Update the confidence of related assumptions.
- If the research overturns the direction, rerun the decision gate.
