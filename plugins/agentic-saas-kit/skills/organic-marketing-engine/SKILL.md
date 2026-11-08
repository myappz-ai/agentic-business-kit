---
name: organic-marketing-engine
description: Sets up a brand's hands-free Instagram organic marketing engine on SaaS Universe. It posts 3 carousels a day, and each post gets a comment keyword, its own free guide page, and its own Social Flow that DMs the guide and saves the commenter as a tagged CRM contact. A nightly review rewrites the strategy from real numbers. Use when someone says "setup my organic marketing engine", "set up Instagram autopilot", "comment-to-DM guides", or "copy the 3-posts-a-day flow for my brand".
---

# Organic Marketing Engine

Run this in four phases, in order. Do not skip the audit. Do not schedule anything until the first post has passed a live end-to-end test.

The content changes per brand. The flow never changes: **post → keyword → unique guide → per-post Social Flow → CRM contact → nightly review**.

## Phase 0 – Brand intake

1. Identify the brand's SaaS Universe sub-account connector: the MCP whose `get_business_profile` returns this brand. Every guide, flow and CRM write goes there. Never use another brand's connector.
2. Collect the answers with AskUserQuestion. Only ask for what the profile or Instagram can't tell you:
   - the Instagram handle
   - the audience
   - the 3 pillars, defaulting to: 08:00 core expertise, 13:00 universal/uplifting for that audience, 20:00 sales and growth
   - the owner's name, title and photo for slide headers
   - the bonus-block offer and URL (no dates, no prices)
   - the guide skin: post, editorial or night
   - the reports channel
   - timezone
   - competitors never to feature
3. Get the owner's standing authorization **in their own words**. For example: "Post every day without my approval; for every guide, turn on the Social Flow by default for each post." Record the exact quote and the date. Every scheduled prompt quotes it.

## Phase 1 – Readiness audit

Follow `references/readiness-audit.md`. Report one table (✅ / ⚠️ / ❌ with evidence) and save it to the project.
- Stop if Instagram isn't connected with DMs ready, or if Composio isn't connected to the **brand's** handle.
- Tell the owner exactly what to click, then re-run the audit when they're done.

## Phase 2 – Build

1. **Guides site**: create it in the brand's sub-account, with a hub page and `references/guide-template.html` as the base (see `references/guide-and-flow-spec.md` §1–3). Publish and verify with `get_page_html`.
2. **Baseline**: pull the last 30 posts and their insights. Find the median reach and the top posts. Seed the Topic Bank from the winners, with at least 5 topics per slot, each with a KEYWORD and a guide idea.
3. **LOCKED doc**: fill `references/locked-doc-template.md` and save it to the project as `LOCKED_<Brand>_IG_Engine.md`.
4. **First post, attended**:
   - Write it using `references/content-rules.md` (a "7 …" list, 10 slides, keyword on caption line 2).
   - Build its guide.
   - Render it with `references/renderer_v3_postcard.py` or `renderer_v5_bigtype.py`; `qa()` must return `[]`.
   - Show the slides, caption and guide to the owner once, for this first post only.
   - Publish it per `references/publishing.md`.
   - Create the flow per `references/guide-and-flow-spec.md` §4, then run `test_social_flow`.
5. **Live test**: the owner comments the keyword from a **different** account. Confirm with `get_social_flow_logs` that the DM was sent, and that a CRM contact exists tagged `ig-<keyword>`. Not done until this passes.

## Phase 3 – Schedule

Create the tasks from `references/scheduled-task-prompts.md` with `create_trigger`:
- 3 slot tasks
- 1 nightly review
- the backstop check (`send_later`, chained)

Each prompt quotes the owner's authorization verbatim. Tell the owner, in one sentence per task, which approval setting it got.

## Phase 4 – Hand over

Send the owner a short summary covering:
- the audit result
- the guides site link
- the first post plus its test result
- the schedule
- where reports arrive
- the known issues from `references/known-issues.md`

Save everything to the project.

## Rules that never change

- **Always give exact, clickable links** (see `AGENT_RULES.md`). After every post, end with the links to the live Instagram post, its guide page and its Social Flow.
- **One flow per post, linked to that post's unique guide.** Never use an account-wide default flow.
- Create the flow immediately after publishing; flows don't replay earlier comments.
- Kind tone, never put the reader down.
- Facts only from pages actually opened.
- No income promises, no fake discounts, no "first-ever".
- No scraping of phone numbers. No bulk Instagram DMs. No passwords.
- Never auto-publish paid ads; this skill is organic only.
- Only the two house styles. Illustrated and photo-strip carousels are rejected.
- Verify the Composio Instagram username before every publish.
- Never post twice in one slot.

## Done when

- [ ] Audit green and saved
- [ ] Guides site live, with a hub
- [ ] LOCKED doc saved
- [ ] First post live; `test_social_flow` would_fire:true; a live comment from a second account produced the DM and a tagged contact
- [ ] 3 slot tasks, nightly review and backstop scheduled, with the owner's authorization quoted
- [ ] Hand-over summary sent
