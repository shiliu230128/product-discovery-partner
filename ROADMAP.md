# Roadmap

## v2.0 — Delivered

- Renamed and repositioned the project as **Product Discovery Partner**.
- Adaptive eight-slot interview engine with quick, standard, and deep modes.
- Jump, backfill, checkpoint, and resume support.
- Evidence ledger with E0–E3 levels, source rules, and contradiction handling.
- Decision gate with CONTINUE / NARROW / PIVOT / PAUSE / STOP and kill criteria.
- Four output tiers: decision memo (one-page brief), lean PRD, full PRD, build spec.
- Validation packs, interview guides, fake-door and concierge templates, and result write-back.
- External research protocol with citations and a no-web fallback.
- Optional China market context module.
- Bilingual Chinese/English references with a manifest and drift check.
- Cleanup of upstream community boilerplate; license and attribution consolidated.

## Next — Quality Evaluation

The current `evals/evals.json` only checks behavior. It does not answer whether the Skill produces better decisions than a strong baseline prompt.

Planned:

1. A fixed rubric covering evidence discipline, specificity, insight quality, MVP discipline, technical feasibility, calibration, decision usefulness, and actionability.
2. A blind pairwise A/B protocol against a baseline “act like a top PM” prompt.
3. Multi-turn cases with hidden personas and answer banks.
4. An anonymized real-transcript regression set.
5. Optional Python harness for running models, blind judging, and reporting win rates with confidence intervals.
6. Human spot-checks of LLM judge results.

Quality bar to define before claiming an advantage:

- Win rate above a pre-registered threshold on a fixed case set.
- No critical failures: fabricated sources, invented quotes, unsafe advice, or a PRD with no evidence.
- Every high-risk claim tagged as verified, assumption, guess, or open.

## Later — Composable Skills

The current Skill keeps discovery, validation, and specification in one installable package. If it grows too large, split along these seams:

- `product-discovery`: interview, evidence ledger, decision gate.
- `validation-designer`: research, validation packs, result write-back.
- `spec-writer`: lean/full PRD and build spec.

Shared handoff artifacts should remain language-neutral: `discovery-state.md`, `evidence-ledger.md`, `decision-memo.md`.

## Later — Product-Type Packs

Add deeper playbooks for:

- AI agents and tool-using products.
- Marketplaces.
- Internal tools.
- B2B SaaS.
- Consumer mobile.
- Regulated products.

Each pack should add decision criteria, metrics, failure modes, and example interviews, not just feature templates.

## Non-Goals

- Becoming a generic PRD template library.
- Maximizing document length or section count.
- Replacing user research, legal advice, or compliance review.
- Claiming quality superiority without a blind evaluation.
