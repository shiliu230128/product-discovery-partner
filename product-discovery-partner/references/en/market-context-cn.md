# China Market Context

This is an optional module. Use it only when the product targets mainland China, involves Chinese platforms/payments/data/content, or the user asks for it.

Regulations and platform rules change. Check the latest official information. This file is not legal advice.

## 1. Clarify First

- Is the target market mainland China, Hong Kong/Macau/Taiwan, overseas, or a mix?
- Where do users enter: WeChat, Douyin, Xiaohongshu, app stores, web, offline?
- Is it for consumers, businesses, government/state-owned enterprises, schools, or hospitals?
- Does it involve payments, invoicing, subscriptions, or prepayment?
- Does it collect personal, sensitive, or minors' data?
- Does it involve content generation, communities, live streaming, e-commerce, finance, healthcare, or education?
- Does the team have China compliance and operations experience?

## 2. Platform Entry Points

| Platform | Good for | Main constraints |
|---|---|---|
| WeChat Mini Program | Lightweight tools, service booking, membership, offline scenarios | Review, category limits, payment/qualification, restricted external links |
| WeChat Official Account | Content, notifications, customer service, private domain | Template-message limits, content review |
| Enterprise WeChat | B2B private domain, sales/support, internal collaboration | Enterprise verification, API permissions |
| Feishu/DingTalk | Internal tools, team collaboration, B2B integrations | Enterprise procurement, permissions, app review |
| Douyin/Xiaohongshu | Content acquisition, seeding, e-commerce | Platform rules, content review, account risk |
| App | High-frequency/deep experience, push, offline | App-store review, privacy compliance, acquisition cost |
| Web | SaaS, tools, SEO, cross-border | Payments, filing, access speed |
| Offline/channel | High-ticket, services, industry customers | Operations-heavy, slower to scale |

Do not launch on multiple entry points at once. Pick the one that best validates the core value.

## 3. Compliance Checklist

Check as applicable:

### Basics

- ICP filing (website/app/mini program per platform requirements).
- Public security filing.
- Privacy policy and user agreement.
- Personal information collection list and consent.
- Account deletion, data export/deletion.
- Protection of minors.
- Content moderation.

### Data

- Personal Information Protection Law (PIPL).
- Data Security Law and Cybersecurity Law.
- Sensitive personal information (biometrics, medical, financial, location, minors, etc.).
- Cross-border data transfer (if using overseas models/cloud).
- Retention period and data minimization.
- Third-party SDK list and data-sharing disclosure.

### AI/Content

- Generative AI service filing / algorithm filing (as applicable).
- Generated-content labeling.
- Content safety review.
- Training data/model source compliance.
- Human review for high-risk content.
- Minor protection mode.

### Industry

- Finance: licenses, risk control, consumer protection, credit reporting.
- Healthcare: internet diagnosis/treatment, medical devices, prescriptions, privacy.
- Education: school licenses, tutoring rules, minors.
- E-commerce/live streaming: business entity, payments, after-sales, advertising law.
- Recruiting/HR: personal information, discrimination, qualifications.

Do not treat “add compliance after launch” as the default. Compliance can change product scope, data flows, and business model.

## 4. Payments and Monetization

- WeChat Pay, Alipay.
- Corporate payments, refunds, reconciliation, invoicing.
- Subscription, usage-based, service fee, one-time purchase.
- Apple IAP (iOS virtual services/subscriptions).
- Mini-program virtual payment restrictions.
- Compliance and refund rules for pre-sales/deposits/membership cards.
- Average revenue, acquisition cost, channel share, gross margin.

Common China B2B models:

- Project/service fee: early high-ticket validation.
- SaaS subscription: standardized, ongoing value.
- Usage/seat-based: team collaboration and APIs.
- Private deployment/customization: large customers, heavy delivery.
- Channel/partner: industry customers, revenue share and training.

## 5. AI Technology Environment

- Domestic model/cloud providers.
- Content safety and moderation APIs.
- Private deployment / domestic technology requirements.
- Model filing and vendor compliance.
- Data residency and cross-border restrictions.
- Cost, latency, concurrency, and rate limits.
- Domestic chip/OS adaptation for government/enterprise.

If using overseas models/APIs, confirm cross-border data, network reliability, and compliance first.

## 6. Growth and Distribution

- Private domain: Enterprise WeChat, communities, Official Accounts, personal accounts.
- Content: Xiaohongshu, Douyin, Video Accounts, Zhihu, Bilibili.
- Search: Baidu, WeChat Search, Xiaohongshu search.
- Channels/partners: industry service providers, system integrators, associations.
- Offline: expos, salons, parks, industry events.
- App store/mini-program search.
- Sales-led: B2B high-ticket, tenders, procurement.

Growth assumptions must match the product type. A consumer content product or mini-program tool has a very different acquisition model from a B2B private-deployment project.

## 7. Impact on the Product

China context may change:

- Platform choice: mini program before app.
- Payment and subscription design.
- Data architecture: domestic storage, permission isolation, audit.
- AI vendor choice.
- Content moderation and human operations.
- Acquisition channels and growth loops.
- Pricing and invoicing.
- Delivery model: SaaS, private deployment, project-based.
- Compliance cost and timeline.

State in the PRD:

- Applicable regions.
- Required licenses/filings.
- Data flow and storage location.
- Payments/invoicing.
- Content moderation.
- Human operations.
- Compliance risks and timeline.

## 8. Questions to Ask the User

- Where do your first users come from?
- Must the product run inside WeChat/Enterprise WeChat/Feishu?
- Does it involve payments, invoicing, subscriptions, or prepayment?
- Does it collect personal, sensitive, or minors' data?
- Does it use overseas models/cloud? Does data need to cross borders?
- Does it need generative AI filing / algorithm filing?
- Are there industry licenses or qualifications?
- Who handles content moderation and customer support?
- Are you open to private deployment/project-based delivery?
- What are the compliance budget and timeline?

## 9. Common Mistakes

- Building an app first, then discovering users are all in WeChat.
- Ignoring mini-program category and payment restrictions.
- Using overseas models for sensitive data.
- No privacy policy or account deletion.
- Generative AI without content moderation and labeling.
- Leaving invoicing, refunds, and reconciliation until after launch.
- Underestimating filing, qualification, and review time.
- Using consumer growth tactics for B2B projects.
