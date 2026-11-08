# Campaign build on Meta (Meta Ads MCP)

Verify every field with `ads_get_field_context` before you use it. Read back after every write. **Everything stays PAUSED / draft until the owner says "go ahead" for that specific launch.** Approving a concept is not a go.

## 0. Identify
- `ads_get_ad_accounts`: confirm the client's ad account. Never use the agency's or the owner's personal account.
- `ads_get_ad_account_pages` / `ads_get_ig_accounts`: the client's Facebook Page and Instagram. Always pass the brand's `instagram_user_id`, so ads run as the brand and never as a personal profile.
- `ads_get_datasets`: the pixel / dataset, for reference. Lead-form campaigns optimise on on-Meta leads.

## 1. Plan (show the owner before building)
- **Offer and funnel chain:** see `funnel-chains.md`.
- **Budget:**
  - Test: ₹1,000–1,500/day per ad set (or the local equivalent), 2–3 ad sets.
  - Scale only what produces real qualified leads.
- **Targeting:**
  - The client's service area as city radii; location type "home + recent".
  - An age band that fits the buyer; languages that match the creative.
  - Placements: Facebook feed, story and reels; Instagram feed, story, explore and reels.
  - **No Audience Network.** It produces cheap, junk leads.
- **Naming:**
  - Campaign: `<BRAND> | LeadForm | <Offer> | <Mon YYYY>`
  - Ad set: `<Audience/Geo> | <Budget>`
  - Ad: `<Concept>-<Format>-<v#>`
- **UTMs** on any website URL:
  - `utm_source=facebook&utm_medium=paid&utm_campaign=<campaign id>&utm_term=<ad set id>&utm_content=<ad tag>`

## 2. Build (drafts)
1. `ads_create_campaign`: objective **OUTCOME_LEADS**, status PAUSED. Use CBO for scaling or ABO for testing.
2. `ads_create_ad_set`, status PAUSED:
   - optimisation = leads, destination = instant form
   - targeting and placements as planned (Audience Network excluded)
   - attribution 7-day click / 1-day view
3. Creatives:
   - Upload with `ads_creative_upload_media` (or `ads_creative_upload_local_image`).
   - Then `ads_create_creative` with the Page, `instagram_user_id`, primary text, headline and CTA (e.g. SIGN_UP / GET_QUOTE / BOOK_NOW).
4. `ads_create_ad`: one per creative, status PAUSED.
5. **Instant form:** build it and attach it to each ad in Ads Manager (see `instant-form-sop.md`). Do not publish.
6. `ads_get_ad_preview` for each ad, then read back every id, budget, placement and form.

## 3. Show the owner
Present it as one table: campaign, ad sets (budget, targeting, placements), ads (creative + copy + form), and the sub-account readiness (pipeline, workflow, templates, test lead).

## 4. Launch (only after "go ahead")
- `ads_activate_entity` for the campaign, ad sets and ads, by id.
- If the launch changes other budgets, change them in the same step and say so.
- Read back `effective_status` for every object.
- Log one line: `date | brand | ad account | change | ids | approved by`.

## Creative and copy rules
- Use the owner's real photos only. Never alter faces with AI.
- One promise per ad, and the form repeats it.
- Structure: pain hook, 3–4 benefit ticks, a "no tech skills needed"-type reassurance where true, then the CTA.
- **No dates or times in ad copy**, so ads can run for months.
- No invented testimonials, results or "verified" claims. No income guarantees. No competitor brand names. Any struck-through price must be real.
- Video reels are usually the strongest. Check before pausing any video.
- Look at competitors with `ads_library_search` before writing concepts.
