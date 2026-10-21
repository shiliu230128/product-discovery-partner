# AI Product Playbook

The core AI product question is not “which model?” It is “is AI necessary, how wrong can it be, and what happens when it fails?”

## 1. Is AI Necessary

Ask first:

- Can the problem be solved without AI?
- Is AI the core value or an efficiency layer?
- Will users accept uncertainty?
- How much does an error cost?
- Are rules, search, templates, or workflow automation already sufficient?

If a traditional approach solves 70% of the problem, do not add a model just to call the product “AI-native.”

A simple test: does AI create a 10x outcome, or just replace a button with a chat box?

## 2. The Role of AI

Common roles:

- Generate: copy, code, reports, images.
- Summarize: meetings, documents, feedback, conversations.
- Search: find answers across large corpora.
- Recommend: suggest the next action.
- Judge: classify, score, review.
- Plan: decompose tasks, prioritize.
- Execute: call tools to complete actions.
- Collaborate: work alongside the user.

Different roles need different quality bars. Generation is judged by usability and editing cost; judgment by accuracy/recall; execution by permissions, audit, and rollback.

## 3. Quality and Evaluation

Define:

- Accuracy / recall.
- User usability rate.
- Human correction rate.
- Hallucination rate.
- Average latency.
- Cost per task.
- Failure recovery rate.
- Miss rate for high-risk errors.

Eval set requirements:

- Start with 20–50 real or anonymized samples.
- Cover common, edge, and high-risk scenarios.
- Define key fields and pass criteria.
- Keep failure samples as regression tests.
- Have target users judge whether the result is usable, not only the technical team.

If these standards are undefined, the PRD must mark AI capability as a high-risk assumption, not a default.

## 4. Failure Handling

When AI fails, you can:

- Show uncertainty.
- Ask the user to confirm.
- Provide citations.
- Allow editing.
- Fall back to a template or rules.
- Route to a human.
- Save a draft instead of executing.
- Limit the output scope.
- Explain “why.”

High-risk scenarios default to “suggestion → user confirmation → execution,” not full automation.

## 5. Human Confirmation and Automation Boundaries

High-risk actions include:

- Sending messages, email, or publishing content.
- Modifying production data.
- Charging, refunding, or transferring money.
- Deleting data.
- Calling external systems with irreversible effects.
- Making high-stakes medical, legal, financial, or employment judgments.

These actions require human confirmation by default, unless the user explicitly asks otherwise and risk is controlled.

Automation levels:

1. Suggest only.
2. Generate a draft; execute after user confirmation.
3. Auto-execute in low-risk, reversible scope.
4. Fully automate, with audit, limits, rollback, and alerts.

Do not jump from level 1 to level 4.

## 6. Agent Boundaries

Agent products must define:

- Which tools it can call.
- Which tools it cannot call.
- Which actions need user confirmation.
- How every step is logged.
- How to undo.
- How to limit cost.
- How to handle loops, timeouts, and failures.
- How to prevent prompt injection and privilege escalation.

An Agent is not “a smarter chat box.” It needs a task state machine, permission boundaries, audit logs, and failure recovery.

## 7. RAG Judgment

RAG fits when:

- Answers must be grounded in private knowledge.
- Citations are required.
- Data changes frequently.
- Fine-tuning is inappropriate.

RAG must handle:

- Data sources and permissions.
- Chunking and metadata.
- Retrieval and reranking.
- Citations.
- Answer confidence.
- Permission filtering.
- Eval set.
- User feedback loop.

The core RAG experience is not “it can answer.” It is “the answer is trustworthy.” RAG without citations and permission filtering becomes an expensive hallucination amplifier.

## 8. Model Selection

Do not assert the latest model capabilities, prices, or context limits from memory. When the user needs current information, say it must be verified online.

Evaluate models by:

- Text/image/audio/video/code.
- Long context.
- Latency.
- Cost.
- Privacy and data residency.
- Tool calling.
- Structured output.
- Reliability.
- Vendor lock-in and migration cost.

The model is not the moat. Data, workflow, distribution, trust, and the evaluation loop are more likely to be.

## 9. Cost and Latency

Estimate:

- Tokens and cost per task.
- Peak concurrency and rate limits.
- Average and p95 latency.
- Retry and failure cost.
- Human review cost.
- Storage and vector retrieval cost.

If unit economics do not work, the product loses more money as it grows. Set cost ceilings and degradation strategies early.

## 10. Data and Privacy

- What data is collected, and why.
- Who can access it.
- Whether it is used for training, and whether users know.
- Whether it crosses borders.
- How long it is retained and how it is deleted.
- Whether it contains sensitive personal information.
- The data-processing terms of third-party models/APIs.

Do not send user data to external models by default. For sensitive data, confirm compliance and user consent first.

## 11. Safety and Content Boundaries

- Prompt injection and unauthorized tool use.
- Harmful content, misinformation, impersonation.
- Protection of minors.
- High-stakes advice (medical, legal, financial, mental health).
- Copyright, voice, and likeness authorization.
- Abuse and bulk generation.

For products involving public figures, voice, identity, finance, healthcare, legal, children, or political content, raise safety, consent, labeling, and compliance questions early.

## 12. China AI Compliance

For the China market, consider:

- Generative AI service filing / algorithm filing (as applicable).
- Content safety review.
- Real-name verification.
- Personal Information Protection Law (PIPL).
- Cross-border data transfer.
- Model/cloud provider compliance.
- Minor protection mode.
- Generated-content labeling.

Regulations and platform rules change. Check the latest official information. This file is not legal advice.

## 13. Common Mistakes

- AI for AI's sake.
- No definition of “how wrong is acceptable.”
- No eval set; judging quality from a demo.
- Letting an Agent execute high-risk actions directly.
- RAG without permission filtering and citations.
- Counting only model cost, not human review and failure cost.
- Treating model capability as the moat.
- Replacing quality design with “the model will improve.”
- Leaving compliance until launch.
