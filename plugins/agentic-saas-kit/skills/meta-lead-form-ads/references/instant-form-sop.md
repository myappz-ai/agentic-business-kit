# SOP: Meta Instant (lead) form

The Meta Ads MCP can create campaigns, ad sets, creatives and ads, but **it has no tool to create an instant form** (checked Nov 2026). Draft every field first, then either build the form in Ads Manager through the browser tools or hand the click path to the owner.

**Golden rules**
1. Never click **Publish**. The ad stays a draft until the owner approves.
2. The form must match the ad's offer: one form per offer.
3. Use the **client's own** privacy policy URL, as a web page (not a PDF or image).
4. The form isn't done until a test lead reaches the CRM with its tag, deal, owner and messages.

## 1. Draft the form (show the owner, get a yes)
| Field | Rule | Example |
|---|---|---|
| Form name | Internal: `<Brand> · <Funnel> · <Mon YYYY>` | BrightPath · Bali packages · Nov 2026 |
| Form type | **More volume** by default. **Higher intent** (+ phone OTP) only if lead quality is the problem. Rich creative for brand-heavy offers | More volume |
| Flexible delivery | Optimised | Optimised |
| Intro headline | ≤ 60 characters; repeats the ad's promise | Plan your Bali trip with a local expert |
| Intro description | What happens after they submit | Share your details; we'll call you within 24 hours. |
| Contact-info description | How the details will be used | Used only to contact you about this trip. |
| Fields | **Full name, Phone (required), Email (optional)** plus at most one qualifier the pipeline actually uses. Delete Meta's suggested extras | Name · Phone · Email (optional) |
| Privacy policy | Client's own URL | https://<client-domain>/privacy-policy |
| Ending headline | Confirmation | Thanks, you're all set. |
| Ending description | **Required by Meta.** Say what happens next | Our team will WhatsApp you within 24 hours. |
| Ending action | By funnel (§3) | Chat on WhatsApp |

## 2. Click path in Ads Manager
Take a screenshot before each step. If no browser is connected, send these steps to the owner and wait.
1. Ads Manager → select the right ad account (`act=<id>`) → open the Leads campaign.
2. Open the ad set (check location, age and placements) → open the ad → **Edit**.
3. Destination → **Instant form** → **+ Create instant form**.
4. Form type tab: enter the form name; keep **More volume** unless Higher intent was agreed; Flexible delivery = Optimised. → Next.
5. Intro: background image off unless a brand image was provided; Greeting on; enter the headline and description. → Next.
6. Questions: enter the contact-info description. Drag Full name to the top. Tick **Optional** on Email. Keep Phone required. Delete the suggested extras with the bin icon. → Next.
7. Privacy: paste the client's privacy URL (the link text auto-fills). → Next.
8. Ending: headline, **description (required)**, then the action plus its link and CTA text. → **Create form**.
9. Confirm "Your form has been added" and that the form is selected on the ad. **Do not publish.** Report back.

## 3. Ending action by funnel
| Funnel | Action | Link |
|---|---|---|
| Appointment (virtual / visit / demo class) | **Book time** | The sub-account calendar booking link |
| Tele-calling (insurance, finance, travel packages, education) | **Chat on WhatsApp**, or **Call business** if calls are answered live | Business WhatsApp number |
| Lead magnet / brochure | View file or Go to website | Guide or thank-you page |
| Shop / product | Go to website (promo code only if the offer is real) | Shop or product URL |

## 4. Mistakes to avoid
| Mistake | Fix |
|---|---|
| Form copy doesn't match the ad | One form per offer; headline repeats the ad's promise |
| Agency or platform privacy policy on a client form | Always the client's own |
| Empty ending description | Required; say what happens next |
| Extra fields left in | Each one lowers submissions; keep only what the pipeline uses |
| Clicking Publish during setup | Never; the owner approves the whole campaign |
| Calling it done without a test lead | Done = the test lead is in the CRM with tag, deal, owner and messages |
