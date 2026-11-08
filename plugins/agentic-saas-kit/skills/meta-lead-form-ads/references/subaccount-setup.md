# Sub-account setup (CRM side) – do this BEFORE the ad goes live

All of this happens in the **client's** SaaS Universe sub-account connector. Every write is a preview first, then a confirm with `preview_token` after the owner's yes. Sends (email / WhatsApp) go through AI Suite → Approvals.

## 1. Connections
| Check | Tool | Pass |
|---|---|---|
| Meta connected at sub-account level | `get_ad_connection_health`, `list_ad_accounts` | Right ad account, token valid. Otherwise: Ad Launcher → Platforms → Connect with Meta. |
| WhatsApp (WABA) | `list_waba_connections` | A connected number with quality GREEN and display name approved. A LIMITED number can't send templates reliably. |
| Email sender | `list_smtp_connections` | A verified sender |
| Calendar (appointment funnels) | `list_event_types` / `create_calendar_event_type` | A booking link exists |

## 2. Pipeline
`create_pipeline`: name `<Funnel> · <Mon YYYY>`. Stages follow the chain, for example:
- **Tele-calling:** New lead → Contacted → Qualified → Meeting booked → Won → Lost / Not interested
- **Appointment:** New lead → Booked → Showed → Won → No-show → Lost

## 3. Lead-form sync
- Map the Meta form in the sub-account: Ad Launcher → lead-form sync. There is no `map_lead_form` tool yet, so this is a UI step.
- Confirm the form's leads appear in `list_ad_leads`.

## 4. Templates
- **WhatsApp:** `create_waba_template`, category UTILITY, for the instant reply. Example: "Hi {{1}}, thanks for your interest in {{2}}. {{3}} from our team will call you shortly." It needs Meta approval before go-live; check `list_waba_templates` for APPROVED.
- **Email:** `create_email_template` for the instant confirmation.

## 5. Workflow (speed to lead)
`create_workflow` + `update_workflow_steps`, then `validate_workflow_graph`. Publish with `update_workflow_status` only after the owner's yes.
1. Trigger: lead from this Meta form (or form submission).
2. Create or update the contact. Add tags `fb-leadform` and `<campaign-tag>`.
3. Create a deal at stage 1 of the pipeline, with an owner assigned (round robin if there is more than one caller).
4. Instant WhatsApp (utility template) and the instant email.
5. **Call task due in 5 minutes** for the owner, plus an internal alert.
6. No answer: a day 1 / 3 / 7 follow-up (WhatsApp, then email).
7. Appointment funnels: confirmation, a 24 h reminder, a 1 h reminder and a no-show follow-up.

Look at `query_workflow_templates` first. Reuse a lead-form template if one exists rather than building from scratch.

## 6. Test lead (mandatory)
1. Submit one test lead with Meta's Lead Ads Testing Tool, or a test submission on the form.
2. Read back each item:
   - contact (`query_contacts`) and its tags
   - deal and owner (`query_opportunities`)
   - WhatsApp and email logs
   - the call task
3. Only then is the setup done.
