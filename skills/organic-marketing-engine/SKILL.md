---
name: organic-marketing-engine
description: Sets up a brand's hands-free Instagram organic marketing engine on its own platform account. It posts 3 carousels a day, and each post gets a comment keyword, its own free guide page, and its own Social Flow that DMs the guide and saves the commenter as a tagged CRM contact. The same carousel goes to LinkedIn as a PDF document post with comment replies. A nightly review rewrites the strategy from real numbers. Use when someone says "setup my organic marketing engine", "set up Instagram autopilot", "comment-to-DM guides", or "copy the 3-posts-a-day flow for my brand".
---

# Organic Marketing Engine

Run this in four phases, in order. Do not skip the audit. Do not schedule anything until the first post has passed a live end-to-end test.

The content changes per brand. The flow never changes: **post → keyword → unique guide → per-post Social Flow → CRM contact → LinkedIn PDF copy → nightly review**.

## Setup check (always first)
Call `query_custom_values` with search `agentic_kit_setup`. If it's missing, say "Let's finish your account setup first; it takes about 5 minutes." Then run the **get-started** playbook, and come back here when it's done.

## Phase 0 – Brand intake

1. Identify the brand's platform account connector: the MCP whose `get_business_profile` returns this brand. Every guide, flow and CRM write goes there. Never use another brand's connector.
2. Collect the answers with AskUserQuestion. Only ask for what the profile or Instagram can't tell you:
   - the Instagram handle
   - the audience
   - the industry pack from `references/industry-packs.md` (match it from the profile; ask one question only if two packs fit). It fills the 3 pillars, starter topics, free-resource ideas and keywords.
   - the owner's name, title and photo for slide headers
   - the bonus-block offer and URL (no dates, no prices)
   - the guide skin: post, editorial or night
   - the reports channel
   - timezone
   - competitors never to feature
   - whether LinkedIn is connected (for the PDF copy of every post)
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

   - Post the same slides to LinkedIn as a PDF document per `references/linkedin-crosspost.md`, when LinkedIn is connected.

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

## The daily posting system (what every install runs)

This is the pattern the kit sets up. Follow it exactly; only the topics and the brand change. Details: `references/content-rules.md`, `references/linkedin-crosspost.md`, `references/scheduled-task-prompts.md`.

**1. Three posts a day, two kinds of carousel.**

| Slot (brand TZ) | Kind | Pillar | Built for |
|---|---|---|---|
| 08:00 | White post-card (v3) | The brand's core expertise (tips, tools, how-tos) | Saves and comments |
| 13:00 | Cream big-type (v5) | Universal wisdom and life lessons, told for the audience | Shares and saves |
| 20:00 | White post-card (v3) | Sales and growth for the audience | Comments |

**2. One carousel shape, 10 slides.**
- Slide 1: a "7 …" hook that promises time, money or a clear result, plus the line **"🎁 Free gift on slide 4 →"**.
- Slides 2–3: the first items of the list.
- Slide 4: **the gift preview.** The free resource's title, 3 short teasers of what's inside, a FREE badge, and "Comment KEYWORD and I'll send you the <doc>".
- Slides 5–9: the rest of the list and a "screenshot this" recap.
- Slide 10: the CTA again, plus one save line and one share line.
- Build the free resource page **before** rendering, so slide 4 previews what really exists.

**3. Comment-to-DM on every post.**
- Caption line 2 asks for the comment: "Comment KEYWORD and I'll send you the free <doc>." Always ask for a **comment**, never "DM me".
- Each post gets its own free resource page and its own Social Flow: a friendly public reply, then a DM with the link, once per person, with a CRM tag `ig-<keyword>`. Test it before calling the post done.
- Vary the word for the resource across posts: gift, doc, cheat sheet, guide, checklist, playbook. Keep one word throughout a single post.

**4. Keywords people can type.**
- One common word, 3–8 letters, letters only, uppercase (JAPAN, AGENT, PRICE). No numbers, symbols or made-up spellings.
- A word may be reused on a later post. The comment keyword is matched per post, so each post sends its own resource. Give the new resource its own address (`japan-2`, `japan-3`), and only set the DM keyword when no other active flow already uses that word.

**5. LinkedIn copy of every post.**
- When LinkedIn is connected, the same slides go out as **one PDF document post**, never as single images, so people can save and read the doc.
- The caption says "Free <doc> on page 4" and asks for the keyword in a comment. Reply to each keyword comment in the comment thread with the link. LinkedIn has no automated DMs.

**6. The virality pattern.**
- Lists beat stories. Name a specific tool, outcome, time or money saved.
- Ask for the comment in the first two lines of the caption, above the "more" fold.
- Win on saves and shares: a recap slide, a save line and a "send this to a friend who…" line on every post.
- Nightly: score = reach + 3×comments + 3×shares + 2×saves + likes, compared with the 30-post median. Double down on winners with a "Part 2", drop what loses, keep at least 5 unused topics per slot.
- Kind tone always. Facts only from pages actually opened. No income or result promises.

## The brand's own style (saved in the account)

Three layers, read in this order every run:
1. **The method** (this skill): the same for everyone; changed only by the kit's maintainers with evidence.
2. **The industry pack** (`references/industry-packs.md`): the starting topics for that industry.
3. **The brand's style**: its voice, audience, pillars, offer, used keywords and its own learnings. It always wins over the pack.

Save the brand's style in the account with `set_custom_value` (name `organic_style`, category `agentic-kit`): a short summary covering voice, audience, pillars, offer, bonus block, competitors to avoid and the top 3 learnings. Keep the full detail in the LOCKED doc. The nightly review updates both. This way the style survives a change of agent and kit updates never overwrite it.

## Adding what works

A new practice goes into the method or a pack only when the numbers prove it:
- It beat the brand's 30-post median score, on at least 2 businesses, over 30+ posts.
- Write the evidence next to the rule (accounts, dates, median vs result), as `references/content-rules.md` does.
- Until then it stays in that brand's own style as a test.

## Rules that never change

- **Always give exact, clickable links** (see `docs/AGENT_RULES.md`). After every post, end with the links to the live Instagram post, its guide page and its Social Flow.
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
- Every carousel announces the free gift on slide 1 and previews it on slide 4.
- Keywords: one easy word, 3–8 letters. A reused word always sends the resource of the post it was commented on.
- LinkedIn gets a PDF document post, never single images.

## Done when

- [ ] Setup check passed (`agentic_kit_setup` exists)
- [ ] Audit green and saved
- [ ] Guides site live, with a hub
- [ ] LOCKED doc saved
- [ ] First post live; `test_social_flow` would_fire:true; a live comment from a second account produced the DM and a tagged contact
- [ ] 3 slot tasks, nightly review and backstop scheduled, with the owner's authorization quoted
- [ ] First post's carousel has the slide-1 gift line and the slide-4 preview
- [ ] LinkedIn PDF copy posted (or LinkedIn marked ⚠️ not connected)
- [ ] Industry pack applied and `organic_style` saved in the account
- [ ] Hand-over summary sent
