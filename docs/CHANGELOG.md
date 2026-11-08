# Changelog

## 0.3.8 – 8 Nov 2026
- organic-marketing-engine documents the full daily posting system: 3 posts a day in two carousel kinds, the 10-slide shape with "Free gift on slide 4" on slide 1 and a gift preview on slide 4, comment-to-DM on every post, the virality pattern and the nightly score.
- Keyword rules: one easy word (3–8 letters); reuse allowed with per-post flows, numbered resource addresses and DM keywords only when unused.
- New `references/linkedin-crosspost.md`: every carousel also goes to LinkedIn as a PDF document post, with in-thread replies.
- Scheduled slot prompts updated to match.

## 0.3.7 – 8 Nov 2026
- get-started reads shared documents (tax or registration certificates, invoices, visiting cards) and fills the profile from them. Fields with no tool are sent to the screen and reported as a platform gap.

## 0.3.6 – 8 Nov 2026
- get-started asks for tax and registration IDs by country (GSTIN/PAN, EIN, VAT, TRN, ABN, BN, UEN and others), never assumes India, and sets currency and timezone to match.

## 0.3.5 – 8 Nov 2026
- get-started harvests everything a website already shows (social links, logo, booking link, hours, contact, legal name) and never asks for it again. Saves social links as account custom values until the profile has fields for them.
- A company name alone is enough: the agent searches for the website, registry record and social pages, and asks "Is this you?" only when names clash.

## 0.3.4 – 8 Nov 2026
- get-started asks for the business website first and prefills the brief, profile and logo from it.
- One "go" from the user covers the whole setup pass; no field-by-field questions. Sending, publishing and spending still need their own yes.

## 0.3.3 – 8 Nov 2026
- get-started Step 3 now completes the **whole Business Profile** (type, website, registered address, tax id, currency, representative contact), re-reads it after saving, and never trusts the completeness score alone.
- get-started Step 4 now checks the App Store and separates **required** connections (AI model, email, WhatsApp, calendar when customers book) from optional ones.

## 0.3.2 – 8 Nov 2026
- get-started, from the first live new-client test (sample dental clinic):
  - Step 1 handles a new account with a placeholder name.
  - Step 3 saves the business profile together with the brief on one "yes", and has a logo fallback (inline upload when the upload link fails; a placeholder mark when the client has no logo).

## 0.3.1 – 8 Nov 2026
- New rule 4 in `AGENT_RULES.md`: **connection order** (platform account → official connectors → Composio or anything the user already uses). Never block a working Composio setup. Explain each connection in one plain line.
- `CONNECTORS.md` reorganised by that order. get-started checks connections in that order.

## 0.3.0 – 8 Nov 2026
- New **get-started** playbook: the mandatory first-run setup. It connects the account, syncs the business brief, checks Instagram, Meta, WhatsApp, email and calendar, applies the house rules, saves `agentic_kit_setup` in the account, and recommends the first playbook.
- Every playbook now starts with a setup check, and runs get-started first if setup isn't done.
- Claude: a first-chat nudge (session-start hook) asks new users to say "Get started".
- Simpler front page: a 3-step "Start here". Technical files moved into `docs/`.

## 0.2.0 – 8 Nov 2026
- Renamed to **Agentic Business Kit** (was Agentic SaaS Kit). The install command is now `/plugin install agentic-business-kit@agentic-kits`.
- White-label ready: no platform or company brand names inside the playbooks. Your agency's or platform's name is never shown to clients.
- The kit now sits at the repository root (`skills/`, `AGENT_RULES.md`, …), so the Agentic Agency Kit can include it directly.

## 0.1.1 – 8 Nov 2026
- New `AGENT_RULES.md`, which every agent (Claude, ChatGPT, Grok and others) follows. The first rule: always give exact, clickable links, take them from tool results or opened pages, and never invent them.
- All three skills now say which links to give after each step.

## 0.1.0 – 8 Nov 2026
- **organic-marketing-engine:**
  - 3 posts a day, with a keyword, a unique guide and a per-post Social Flow on every post.
  - Readiness audit, guide template (3 skins), v3 and v5 renderers with QA, scheduled-task prompts (slots, nightly review, backstop), LOCKED doc template and known issues.
  - Proven on a ~26K-follower creator account, 7–8 Nov 2026: flows delivered DMs within ~2–10 s, and tagged contacts were created.
- **meta-lead-form-ads:**
  - Industry funnel chains, sub-account setup (pipeline, templates, speed-to-lead workflow), Meta draft build, instant-form SOP, test-lead gate, go-ahead launch, and daily reporting with RED flags.
  - From live ad operations for a SaaS business and a marketplace, Oct–Nov 2026.
- **add-proven-playbook:** how to add new proven flows to the kit.
