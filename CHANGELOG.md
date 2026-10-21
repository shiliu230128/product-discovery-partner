# Changelog

## 2.0.0 — 2026-10-21

### Changed

- Renamed the project and Skill to **Product Discovery Partner**.
- Replaced the linear ten-stage interview with an adaptive eight-slot interview engine.
- Added quick, standard, and deep modes with question budgets and fatigue handling.
- Added jump, backfill, checkpoint, and resume support.
- Added an evidence ledger with E0–E3 levels, source rules, confidence, and contradiction handling.
- Added a decision gate with CONTINUE / NARROW / PIVOT / PAUSE / STOP outcomes and kill criteria.
- Replaced the default 25-section PRD with four output tiers: decision memo, lean PRD, full PRD, and build spec.
- Added validation packs, fake-door/concierge/interview templates, and validation result write-back.
- Added external research protocol with citation rules and a no-web fallback.
- Added an optional China market context module.
- Added anti-sycophancy rules and an explicit STOP path.
- Added Chinese/English reference parity checks via `scripts/check-i18n.py`.
- Consolidated documentation and removed upstream community boilerplate from the project root.
- Updated the license attribution and added `NOTICE.md`.

### Deferred

- Blind A/B quality evaluation.
- Python evaluation harness.
- Anonymized real-transcript regression set.
- Splitting the Skill into composable sub-Skills.

## 0.1.0

- Initial public version of Product Idea Excavator.
- Added core Skill instructions.
- Added PRD template.
- Added product sense, technical stack, and AI product playbooks.
- Added sample run and starter evals.
