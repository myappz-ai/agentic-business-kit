# Guide page + Social Flow spec (one per post)

**Every post gets its own guide and its own flow, linked to that post.** There is never an account-wide default flow, because each guide is unique.

## 1. Guides site (built once per brand)
- Create it in the **brand's** sub-account with `create_funnel`, named "<Brand> Free Guides", type website.
- Hub page: `index`, a list of guide cards, newest first.
- Template: `guide-template.html` in this folder. Fill every `{{…}}` and delete any unused optional blocks.
- Skins: `post` (white), `editorial` (cream, serif headings) or `night` (dark with a yellow bonus). Use one skin per brand, chosen once.
- Guide URL pattern: `https://<SITE_DOMAIN>/site/<funnel-slug>/<keyword-lowercase>` (use the exact URL the publish tool returns; white-label accounts have their own domain).
  - The live URL renders client-side, so a plain fetch returns an empty shell.
  - To verify the content, use `get_page_html`.

## 2. Guide content (3 pages max)
1. **Hook**: title promise; chips for read time, "🔗 N free resources" and "🎁 Bonus on page 3"; a "Watch first" box (the owner's own video, or "How to use this guide"); a short "Why now".
2. **Playbook** ("screenshot this"): 5–7 steps. Each step has a **How:** line, plus a copy-paste template or a resource link where useful. End with the strip "Toolkit + bonus →".
3. **Toolkit + bonus**:
   - 4–6 resource cards (GUIDE / PDF / REPO / DOCS / VIDEO / CASE)
   - the brand's universal bonus block
   - a share line in the footer

Resource rules:
- Open every link before using it; it must load and its title must match.
- Prefer official docs, official GitHub repos and the owner's own content.
- No affiliate or unverified links.

**Bonus block (universal per brand, set once in Phase 0):**
- No dates, event names or prices. It must stay true for someone who comments months later.
- No struck-through price unless that price is real.
- Pattern: ribbon "YOUR BONUS", one headline, one line of body copy, a button ("Claim the event link →", "Get your free audit →", …), and the destination URL with `utm_source=instagram&utm_medium=guide&utm_campaign=<keyword>`.
- If the destination ever changes, only the URL changes.

## 3. Building the page (brand's sub-account connector)
Each write is a preview first. Then call again with `preview_token` and `confirm:true`; the owner's standing authorization covers it.
1. `create_page`: funnel = the guides funnel, name = the guide title, page_slug = keyword in lowercase.
2. `write_page_html` with the filled template.
3. Add a card to the hub page `index`: `get_page_html`, insert the newest card first, then `write_page_html`.
4. `publish_site` with `rebuild:true`.
5. Verify with `get_page_html` on the new page.

## 4. Social Flow fields (`create_social_flow`, brand's sub-account connector)
| Field | Value |
|---|---|
| post | the media_id (just published) |
| account | the brand's IG username (when more than one is connected) |
| trigger | `{"comment_keywords":["KEYWORD"],"dm_keywords":["KEYWORD"]}`. Comment keywords are per post, so a reused word is fine. DM keywords are account-wide: set them only when no other active flow uses the word (`list_social_flows`), otherwise `[]`. A reused word gets a numbered resource address (`japan-2`). |
| public_reply_variants | 3–4 short, friendly replies, e.g. "Sent! Check your DMs 📩", "Done ✅ Look in your DMs" |
| dm_message | "Here's your free <guide name> 📘 <one line on what's inside>. Tap below 👇" (max 640 characters) |
| attachment | `{"url": "<that post's guide URL>"}` |
| button_label | "Get the guide" (max 20 characters) |
| crm | `{"tags":["ig-<keyword-lowercase>"]}` |
| once_per_person | true |
| follow_gate | `{"enabled": true, "message": "Almost there! 🙌 Follow @<handle>, then reply DONE here and I'll send your free <guide name> 📘"}`. **On by default.** The guide is sent only after the follow is verified. The platform currently waits for the typed word "done", so the message must say "reply DONE". |

Then:
- `test_social_flow` with the comment "KEYWORD please". It must return `would_fire: true`.
  - The dry run covers the first DM only. The follow check after "done" can only be confirmed live.
- **Live test (first post for each brand only):** someone comments the keyword from a *different* Instagram account. Comments from the brand's own account never trigger a flow.
  - Check `get_social_flow_logs`: `dms_sent ≥ 1`, `contacts_linked ≥ 1`.
  - Check the contact exists in the CRM with tag `ig-<keyword>`.

## 5. Facts to remember
- A flow only reacts to comments made **after** it is created. Earlier comments are not replayed.
- Meta rules: no DMs to comments older than 7 days. DMs over the hourly limit are queued.
- Bulk Instagram DMs are not supported. Never scrape phone numbers from profiles.
- Until the button version of the follow gate ships, every commenter is asked to follow, including existing followers, and only the typed word "done" confirms.
- `create_short_link` is broken (missing `is_active` column). Use full URLs.
