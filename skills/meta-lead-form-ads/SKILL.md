---
name: meta-lead-form-ads
description: Sets up and launches Meta (Facebook/Instagram) lead-form ad campaigns for a brand, end to end, on Meta and in the brand's platform account. It covers the funnel choice, the CRM pipeline, form sync, the speed-to-lead workflow, WhatsApp/email templates, draft campaigns, the instant form, a test lead, the launch on go-ahead, and daily reporting. Use when someone says "launch lead form ads", "setup Meta lead ads", "run instant form campaign", or "get leads from Facebook ads into my CRM".
---

# Meta Lead-Form Ads

Build the CRM side first and the ads second. Nothing goes live until two things are true: a test lead has reached the CRM with its tag, deal, owner and messages, and the owner has said "go ahead" for that specific launch.

## Phase 0 – Intake
Collect what's missing with AskUserQuestion:
- business type, offer, and service area (cities or radius)
- target cost per lead and daily budget
- who calls the leads, and when
- the client's privacy-policy URL
- WhatsApp number
- creatives available (real photos or videos)
- the owner's approval channel

Use the brand's own sub-account connector: confirm with `get_business_profile`. Pick the funnel chain from `references/funnel-chains.md`, recommend the default, and confirm it.

## Phase 1 – Readiness audit
Report one ✅ / ⚠️ / ❌ table with evidence:
- **Meta MCP:**
  - `ads_get_ad_accounts`: the client's ad account is active and has a payment method
  - `ads_get_ad_account_pages` / `ads_get_ig_accounts`: the brand's Page and Instagram
- **Sub-account:**
  - `get_ad_connection_health`
  - `list_waba_connections`: quality GREEN, display name approved
  - `list_smtp_connections`
  - a calendar, if the funnel books appointments
  - an existing pipeline or workflow to reuse
- **Privacy:** the client's privacy-policy page loads.

Stop on any ❌ and tell the owner exactly what to connect.

## Phase 2 – CRM side
Follow `references/subaccount-setup.md`: pipeline → templates (WhatsApp UTILITY, email) → speed-to-lead workflow (instant WhatsApp and email, a call task in 5 minutes, an owner alert, nurture on day 1 / 3 / 7, show-up reminders) → validate. Preview every write and confirm only after the owner's yes.

## Phase 3 – Meta side (drafts only)
Follow `references/campaign-build.md`:
1. Plan budget, targeting (no Audience Network), naming and copy, and show it to the owner.
2. Create the campaign (OUTCOME_LEADS), ad sets, creatives and ads, all PAUSED.
3. Draft the instant form per `references/instant-form-sop.md`, get a yes, then build and attach it in Ads Manager (browser tools, or hand the click path to the owner). Never click Publish.
4. Map the form in the sub-account's lead-form sync (a UI step).

## Phase 4 – Test lead
Submit one test lead (Meta Lead Ads Testing Tool), then read back:
- the contact and tags
- the deal at stage 1, with its owner
- the WhatsApp and email logs
- the call task

Fix anything missing. This step is mandatory.

## Phase 5 – Launch (only on "go ahead")
1. `ads_activate_entity` by id.
2. Read back `effective_status`.
3. Log the change.
4. Send the owner one summary: campaign and ids, budget, form, workflow, test-lead result, and where the reports arrive.

## Phase 6 – Report and optimise
Schedule the read-only daily report from `references/reporting.md`, using cost per *CRM* lead, GOOD / HOLD / JUNK, a RED list and one main flag. Recommend changes; don't execute them without a yes.

## Rules that never change
- **Always give exact, clickable links** (see `AGENT_RULES.md`). After each build step, end with the links to the pipeline, workflow, form and Meta campaign draft. Every click-path step gets its own URL.
- **Nothing goes live without the owner's explicit "go ahead" for that launch.** Pausing and budget changes also need a yes.
- Ads run as the brand's Page and Instagram, never as a personal profile.
- No Audience Network. Never pause a video ad without an explicit yes.
- Use the client's own privacy policy. One form per offer. The form repeats the ad's promise.
- Use the owner's real photos untouched. No AI-altered faces.
- No dates in ad copy, no invented claims or testimonials, no income guarantees, no fake strikethrough prices, no competitor names.
- Never put credentials in chat.
- Done = a test lead in the CRM with its tag, deal, owner and messages.

## Done when
- [ ] Audit green
- [ ] Pipeline, templates and workflow live and validated
- [ ] Campaign, ad sets, ads and instant form built as drafts, and form sync mapped
- [ ] Test lead passed end to end
- [ ] Owner said "go ahead"; the campaign is active and read back
- [ ] Daily report scheduled
