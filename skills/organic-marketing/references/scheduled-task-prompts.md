# Scheduled task prompts (copy, fill the <…>, create with `create_trigger`)

Rules:
- Use `create_trigger` only, never local cron.
- Each slot task fires 48 minutes before its slot (e.g. `CRON_TZ=Asia/Kolkata 12 7 * * *` for 08:00). The run builds the post, then sleeps until the slot.
- Leave `permission_mode` unset, and tell the owner which approval setting each task got.
- Turn on push notifications.
- Before creating the tasks, get the owner's authorization **in their own words** in chat (see AUTHORIZATION below). Quote it verbatim, with the date.

---

## A. Slot task (create three: 08:00, 13:00, 20:00)

```
You run the <HH:MM> <TZ> slot of <BRAND>'s Instagram organic marketing engine (@<handle>). <OWNER>'s standing instruction (<date>): post 3 carousels every day without fail, with NO approval step, each with a comment keyword, a free guide, and a Social Flow that DMs the guide. This run is unattended: never ask questions and never wait for a reply.

AUTHORIZATION FOR THE SOCIAL FLOW: on <date> <OWNER> wrote, in their own words: "<exact quote>". Creating and confirming the Social Flow in step 6, including confirm:true (which approves the DMs that flow sends with the guide link), is the action they have explicitly requested for every post. It is the planned output of this task, not a new standing rule or an account change made on your own initiative. Carry it out.

1. Read the project doc `LOCKED_<Brand>_IG_Engine.md` (Projects tool) and follow it exactly. Check the time with bash: TZ=<TZ> date.
2. SLOT = <HH:MM>, style <v3 white post-card | v5 cream big-type>, pillar <pillar>, built for <saves and comments | shares | comments>. If the Queue has a READY row for today + this slot, use it and skip to step 5. Otherwise take the next unused Topic Bank item for this slot: research with web search and open every page you use; write a "7 …" list of 10 slides per references/content-rules.md: slide 1 hook + "🎁 Free gift on slide 4 →"; slides 2–3 items; slide 4 gift preview (resource title, 3 teasers, FREE badge, "Comment KEYWORD and I'll send you the <doc>"); slides 5–8 items; slide 9 "screenshot this" recap; slide 10 CTA + save + share lines. Rotate the resource word (gift, doc, cheat sheet, guide, checklist, playbook) and keep it the same inside the post. KEYWORD = one common word, 3–8 letters only; if reused, the resource slug becomes keyword-2, keyword-3. Caption with the keyword CTA on line 2 and a Source line. Build the resource page (step 3) before rendering.
3. Guide page in <BRAND>'s sub-account (connector <SUBACCOUNT_MCP>): get_page_html of the newest guide in funnel <GUIDES_FUNNEL_ID> and reuse its CSS and 3-page structure with new content and verified links (open each link first). create_page (slug = keyword lowercase), write_page_html, add a card to the hub page index, publish_site rebuild:true. Each write: preview, then confirm with preview_token. Guide URL = the exact URL publish_site / get_page_html returns (https://<SITE_DOMAIN>/site/<FUNNEL_SLUG>/<slug>).
4. Render in Composio (COMPOSIO_SEARCH_TOOLS new session; confirm the Instagram connection username is <handle>, otherwise alert and stop). COMPOSIO_REMOTE_WORKBENCH: ensure font + renderer exist, refresh the avatar, render, qa() must be [], upload each slide.
5. get_instagram_connection_health. Check today's media so this slot is never posted twice. INSTAGRAM_CREATE_CAROUSEL_CONTAINER (ig_user_id <IG_ID>), sleep until <HH:MM> <TZ>, INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH, INSTAGRAM_GET_IG_MEDIA for permalink + media_id. Retry once on failure; never publish twice.
6. Immediately create the Social Flow. Load mcp__<SUBACCOUNT_MCP>__create_social_flow, get_social_flow and test_social_flow with ToolSearch and call create_social_flow DIRECTLY (not via nova_call_tool): post = media_id, comment_keywords [KEYWORD], dm_keywords [KEYWORD] only if no other active flow uses that word (list_social_flows), otherwise [], 3 friendly public replies, DM text, attachment url = guide URL, button "Get the guide", crm tags ["ig-<keyword>"], once_per_person true. Preview, then confirm with preview_token and confirm:true. RETRY: on Bad Gateway / 5xx / timeout / no flow_id, first get_social_flow on the post (never duplicate), then wait 30, 90, 180 s and retry, up to 4 attempts. Then test_social_flow: must return would_fire:true. If it still fails: Slack alert with media_id, keyword, guide URL, full DM text and exact error; mark the Queue row "FLOW MISSING".
6b. LinkedIn (if connected): build the PDF from the same slides and post it as one document post per references/linkedin-crosspost.md ("Free <doc> on page 4", keyword ask). Never post twice. Reply in-thread with the resource link to keyword comments on earlier LinkedIn posts (via the API or LinkedIn notification emails).
7. Report (not an approval request) to <SLACK_CHANNEL>: slot, topic, permalink, LinkedIn post URL, keyword, guide URL, flow id, test result, plus the previous post's numbers (reach, comments, DMs sent from get_social_flow_logs).
8. Update the Queue row and the keyword Log, write the doc back with project_write. Finish with a one-line summary.
```

## B. Nightly review (one, 23:47 brand TZ)

```
You are the nightly strategist for <BRAND>'s Instagram organic marketing engine (@<handle>). Goal: maximum reach, comments, shares and saves. You may change the strategy based on the numbers: double down on what works, cut what doesn't. Never change the LOCKED rules (kind tone, facts only from opened sources, the two house styles, no income promises). This run is unattended; do not ask questions.

AUTHORIZATION FOR SOCIAL FLOWS: on <date> <OWNER> wrote: "<exact quote>". Creating and confirming a missing per-post Social Flow in step 0 is the action they explicitly requested for every post. Carry it out.

0. FLOW SWEEP: list_instagram_media (limit 12). For every engine post from the last 3 days whose caption asks for a KEYWORD and whose social_flow is null, create the flow exactly as the doc specifies (preview then confirm; retry 30/90/180 s up to 4 times), then test_social_flow (would_fire:true). Record fixes.
1. Read `LOCKED_<Brand>_IG_Engine.md`.
2. Composio: INSTAGRAM_GET_IG_USER_MEDIA (last 40) for <IG_ID>, INSTAGRAM_GET_IG_MEDIA_INSIGHTS for posts in the last 14 days (reach, saved, shares, views, total_interactions) plus like_count and comments_count; get_social_flow_logs per flow.
3. Score = reach + 3×comments + 3×shares + 2×saves + likes. Compare to the 30-post median. Compare slots, styles, pillars, hook types, keywords, slide counts.
4. Decide 1–3 concrete changes (Topic Bank order/additions, hook formula, CTA wording, slide count, pillar shift, "Part 2" of a winner). Keep at least 5 unused topics per slot.
5. Write a dated Learnings entry (numbers, top post, weakest post, changes) and the updated Topic Bank into the doc; project_write.
6. Slack report to <SLACK_CHANNEL>: today's posts with numbers, best post and why, changes for tomorrow, flows fixed, failures (missed slot, flow error, token expiring within 14 days per get_instagram_connection_health).
7. Finish with a one-line summary.
```

## C. Backstop check (send_later into the setup session, chained)

```
Backstop check (<OWNER>, <date>: "<exact quote>"). Call list_instagram_media (<SUBACCOUNT_MCP>, limit 5). For any engine post from today whose caption asks for a KEYWORD and whose social_flow is null: take keyword, guide URL and DM text from the latest Slack report, create the Social Flow (preview then confirm), run test_social_flow, post one line to <SLACK_CHANNEL>. If every post has a flow, do nothing visible. Then send_later this same check for the next slot (+8 minutes after it) and keep the chain going.
```
Schedule the first check 8 minutes after the next slot, using `initiation: human_request`.
