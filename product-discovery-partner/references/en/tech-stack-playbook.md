# Tech Stack Playbook

Technical recommendations must serve the product stage, team capability, and risk—not novelty.

## 1. Principles

- **Mature by default:** unless a new technology creates a clear product advantage, prefer what the team can operate, what has a mature community, and what is easy to hire for and maintain.
- **Reversible first:** prefer replaceable choices early. Clearly document irreversible or costly-to-migrate decisions in the PRD.
- **Complete but not overbuilt:** if adding error handling, logging, permissions, tests, and admin only costs a little more, do not defer them.
- **Validate value before scaling architecture:** do not build a complex platform for unvalidated demand.
- **User outcomes first:** the stack serves the product, not technical display.
- **Observability is a product capability:** critical paths must show success, failure, latency, cost, and user behavior.
- **Compliance is part of scope:** for regulated products, confirm licenses, filings, data, and content requirements before choosing architecture.

## 2. Decision Variables to Clarify

- Target platform: web, mobile, mini program, desktop, extension, bot, API-first.
- The team's strongest technologies.
- Launch date, budget, expected scale.
- Data sources, sensitivity, retention period.
- Permissions, audit, compliance.
- Payments, subscriptions, invoicing.
- Real-time collaboration, notifications, offline use.
- Third-party integrations.
- Admin and operations.
- Whether AI is needed, and in what role.
- Which choices are reversible and which are not.
- Which capabilities can be validated manually or semi-manually.

## 3. Reversibility Levels

### Easy to Roll Back

- UI framework and component library.
- Analytics.
- Email/notification provider.
- Static content site.
- Early database schema (with migration tooling).

### Medium Cost

- Database type.
- Authentication.
- Payment provider.
- Cloud provider.
- Frontend/backend split.

### Hard to Roll Back

- Data model and tenant isolation.
- Permission model.
- Core workflow state machine.
- Self-hosted models/private deployment.
- Deep platform integrations.
- Compliance architecture.

For hard-to-reverse decisions, document assumptions, alternatives, and switching costs in the PRD.

## 4. Web SaaS MVP

Default recommendation:

- Frontend: Next.js + TypeScript + React + Tailwind.
- Backend: Next.js API routes / server actions; split services only when necessary.
- Database: Postgres.
- ORM: Prisma or Drizzle.
- Auth: Clerk or Auth.js.
- Payments: Stripe (international) or WeChat Pay/Alipay (China).
- Analytics: PostHog or similar.
- Deployment: Vercel or a cloud platform.
- Monitoring: Sentry + platform logs.

Good for: fast validation, B2B SaaS, AI web products, founding teams.

Quality gates:

- Critical user paths are instrumented.
- Error states are visible to users.
- Admins can fix bad data.
- Important data can be exported.
- Core features have automated tests or a clear test plan.
- Permissions and tenant isolation have a basic design from day one.

## 5. AI Web Products

Default recommendation:

- Web layer: Next.js + TypeScript.
- Model layer: Vercel AI SDK or a similar abstraction.
- Database: Postgres.
- Vector retrieval: start with pgvector; move to a dedicated store at scale.
- File storage: S3/R2/Blob.
- Task queue: add one when long-running jobs appear.
- Evaluation: build a small eval set.
- Cost: log tokens, latency, model, and output quality per call.

Key tradeoff: build the quality loop before building a complex Agent.

Prove early:

- Users will provide real input.
- Output saves real time.
- Users will edit, adopt, or share the result.
- Errors can be detected and corrected.

## 6. AI Agent Products

Must design:

- Tool-calling permissions.
- Task state machine.
- Human confirmation points.
- Retry on failure.
- Audit logs.
- Rollback or undo.
- Cost limits.
- Observability.
- Eval harness.

Do not let an Agent execute high-risk actions without boundaries.

Default safety posture:

- Suggest before executing.
- Draft before publishing.
- Human confirmation before full automation.
- Reversible before irreversible.
- Log every step rather than running a black box.

High-risk actions include sending messages, sending email, publishing content, modifying production data, charging/refunding, deleting data, and calling external systems with irreversible effects.

## 7. RAG Products

Must design:

- Data sources.
- Chunking.
- Metadata.
- Permission filtering.
- Retrieval strategy.
- Reranking.
- Citations.
- Answer confidence.
- Eval set.
- User feedback loop.

An MVP can start with Postgres + pgvector. The core RAG experience is not “it can answer.” It is “the answer is trustworthy.” Permission filtering and citations belong in the product requirements.

## 8. Internal Tools

Default recommendation:

- Earliest stage: Retool / Appsmith / Feishu Bitable.
- Custom: Next.js + Postgres + RBAC.
- Essentials: audit log, permissions, import/export, exception handling.

Principle: do not turn an internal tool into a beautiful but unmaintainable SaaS.

The common failure of internal tools is not an ugly UI. It is missing permissions, exception handling, audit logs, and data-correction capability.

## 9. Mobile Products

Default recommendation:

- MVP: React Native / Expo.
- Strong native needs: Swift / Kotlin.
- Backend: Postgres + API.
- Push: platform push services.
- Analytics: mobile event tracking.

Decide whether native is mandatory:

- Heavy use of system capabilities.
- Extreme performance requirements.
- Complex offline experience.
- Deep background execution, Bluetooth, camera/sensors, etc.

For China, also consider:

- iOS/Android app-store review.
- Privacy policy and permission disclosures.
- Push channels from device vendors.
- Real-name verification and content moderation (if relevant).
- WeChat/Alipay SDK and compliance.

## 10. Enterprise B2B

Prioritize:

- SSO/SAML.
- RBAC.
- Audit logs.
- Data isolation.
- Webhooks.
- Queues.
- Monitoring.
- Backups.
- Compliance path.

Do not promise enterprise capabilities with a consumer-MVP stack.

Layering:

- MVP: basic team permissions.
- V1: audit logs, role permissions.
- Enterprise: SSO/SAML, data isolation, compliance processes, private deployment.

## 11. Marketplace

Technical focus:

- Identity.
- Payments/escrow.
- Reviews.
- Dispute handling.
- Supply/demand matching.
- Operations admin.
- Risk control.

Cold start matters more than technology. The PRD must include an operations strategy and where the first supply and demand come from.

## 12. Workflow Automation

Must design:

- Triggers and events.
- Queues and orchestration.
- Webhooks.
- Retries and idempotency.
- Audit logs.
- Human intervention.
- Failure alerts.
- Permissions and audit.

The more automation, the more you need pause, rollback, and human takeover.

## 13. China Technology Context

For the China market, also consider:

### Platform Entry Points

- WeChat Mini Program / Official Account / Enterprise WeChat.
- Feishu / DingTalk.
- Douyin / Xiaohongshu.
- App / Web.
- Offline/channel.

### Compliance

- ICP filing, public security filing.
- Generative AI service filing / algorithm filing (as applicable).
- PIPL, Data Security Law, Cybersecurity Law.
- Cross-border data transfer.
- Personal information, minors, content moderation.
- Real-name verification.
- Privacy policy, user agreement.

### Payments

- WeChat Pay, Alipay.
- Invoicing.
- Subscription/usage/service fee.
- Apple IAP (iOS virtual services).

### AI

- Domestic model/cloud providers.
- Content safety.
- Private deployment / domestic technology stack.
- Model filing.
- Cost, latency, data residency.

### Growth

- Private domain, Enterprise WeChat, communities.
- Channels/partners.
- Industry events.
- Content marketing.
- App store / mini-program review.

Regulations and platform rules change. Check the latest official information. This file is not legal advice.

## 14. Build Spec Handoff

After the stack is chosen, hand the following to the build spec:

- Platform and deployment topology.
- Data model and permission model.
- APIs/events.
- State machine.
- Third-party integrations.
- Non-functional requirements.
- Monitoring and rollback.
- Test plan.

Do not ask a coding agent to start from “recommended stack.” Give it an acceptance-testable spec.

## 15. Common Mistakes

- Introducing architecture the team cannot maintain because it is “modern.”
- Building a model/vector database/workflow engine too early.
- Missing permissions and tenant isolation, then rewriting later.
- Missing error handling, logs, and admin, so operations edit the database by hand.
- Leaving compliance until launch.
- Promising enterprise security with a consumer stack.
- Choosing technology without tying it to product stage, team capability, and launch date.
