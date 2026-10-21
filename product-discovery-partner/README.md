# Product Discovery Partner

An installable Skill for evidence-driven product discovery. It helps you decide whether an idea is worth building, what the narrowest testable wedge is, and what artifact you actually need—a decision memo, a lean PRD, a full PRD, or a build spec.

It does not jump straight to a PRD. It asks better questions, tracks evidence, runs a decision gate, and can output `PAUSE` or `STOP`.

## Install

Copy this folder into your local Skills directory:

```text
product-discovery-partner/
  SKILL.md
  README.md
  SAFETY.md
  references/
  scripts/
  evals/
  demo/
```

Start a new assistant session so the Skill metadata can be discovered.

## Use

Chinese:

```text
我有一个产品想法，但还很模糊。请用 product-discovery-partner 的方式，通过提问帮我判断该不该做、怎么做。
```

English:

```text
I have a rough product idea. Use product-discovery-partner to interview me, test the evidence, and tell me whether and how to build it.
```

## Modes

| Mode | Questions | Default output |
|---|---|---|
| Quick | About 8 | Decision memo + key assumptions + next validation |
| Standard | 15–20 | Lean PRD + validation pack |
| Deep | 30+ | Full PRD + build spec + AI eval set |

You can jump between topics, backfill new information, checkpoint, and resume.

## Outputs

- Decision memo (one-page brief)
- Lean PRD
- Full PRD (conditional)
- Build spec for coding agents
- Validation pack
- Assumption register

Every factual claim is tagged as verified, assumption, guess, or open question.

## References

Chinese files at the root of `references/` are canonical. English translations live in `references/en/`.

To check for drift:

```bash
python3 scripts/check-i18n.py
```

After updating a translation and confirming it is current:

```bash
python3 scripts/check-i18n.py --update
```

## Evaluation

`evals/evals.json` contains a small legacy behavior suite. A quality/A-B evaluation system is intentionally deferred; do not treat the current evals as proof that the Skill outperforms a baseline.

## Safety

Read [SAFETY.md](SAFETY.md) for boundaries around public figures, voice, identity, high-stakes advice, data, and AI agent actions.

## License

MIT. See the repository `LICENSE` and `NOTICE.md`. When redistributing this Skill, include those files with the skill folder.
