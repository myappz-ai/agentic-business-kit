# Instagram Autopilot in the cloud (laptop closed)

This sets up 3 posts a day, each with its own guide, comment-to-DM flow and follow gate, plus a performance report every night. It all runs as **Claude Code cloud routines**, so your computer can stay off.

## What runs each day (IST)

| Time | Routine | What it does |
|---|---|---|
| 06:15 | Viral watch | Scrapes the creators you track (Apify). Any post with ≥1,000 likes or ≥200 comments becomes an original idea (hook + keyword + slot) in your Slack self-DM. |
| 06:35 | News picks | Scans the OpenAI and Anthropic news and release notes. Posts up to 3 picks with a hook, keyword and slot to Slack. |
| 08:00 | Morning carousel | Playbook carousel → guide page → Social Flow with follow gate → test → LinkedIn PDF → Slack report. |
| 15:00 | Afternoon reel | Takes the next Queued reel from the tracker doc, renders it with an AI avatar (HeyGen), posts it, makes its flow, then posts it to LinkedIn and YouTube Shorts. A carousel is the fallback. |
| 20:00 | Evening carousel | Story or tool-demo carousel, same chain as 08:00. |
| 23:30 | Nightly report | Reach, likes, comments, shares, saves, DMs sent and follows verified for each post, vs your median. It fixes any missing flow or follow gate, catches up missed cross-posts, updates the tracker doc, then suggests one change for tomorrow. |

Topic order for every slot: today's news pick → viral-watch idea → the next row of your 30-day queue.

## One-time setup

1. **Connectors** (claude.ai → Customize → Connectors): SaaS Universe (your sub-account key), Composio (GitHub + Instagram connected), Slack, Apify.
2. **A private GitHub repo** with your own files:
   - `AUTOPILOT.md`: your runbook. Copy the structure below.
   - `queue.json`: 30 days of topics, each with a unique 3–8 letter keyword.
   - `creators.json`: `{"thresholds":{"likes":1000,"comments":200},"accounts":[{"handle":"..."}]}`
3. **A cloud environment** (claude.ai/code → Environments). Cloud routines may not be able to clone a private repo directly (`repo_access_denied`), so each routine prompt fetches the files itself:
   `COMPOSIO_PROXY_EXECUTE` → toolkit `github`, `GET /repos/<you>/<repo>/contents/<file>` → base64-decode `content`.
4. **Create 6 routines** with `/schedule` (cron is UTC, so IST minus 5:30). Give each one all four connectors. Each prompt should say: unattended, never ask questions, fetch the runbook, run step N, report to Slack.

## AUTOPILOT.md structure

- **Standing authorization**, quoted in your own words: for example, "social flow setup is by default for every post, without my approval". Without this, an unattended run stops at the confirm step.
- **State:** a slot is done if an Instagram post exists in its time window. Nothing else to track.
- **Step 0, topic:** news pick → viral idea → queue row.
- **Step 1, hook:** line 1 = the cost of the old way (money or time) or a pain question. Line 2 = one named feature with a concrete result. CTA: "Comment KEYWORD and I'll send you the step-by-step setup guide." Always ask for a comment, never "DM me".
- **Step 2, guide:** publish a guide page on your funnel, with a fixed bonus block that links your offer through a UTM link. No short links, no dates or prices in the bonus.
- **Step 3, post:** render the carousel (kit renderers), or post the queued reel.
- **Step 4, Social Flow:** keyword → DM with the guide link. Follow gate on, message: "Almost there! 🙌 Follow @you, then reply DONE here and I'll send your free <guide> 📘". Retry after 30/90/180 s if the media isn't ready yet. Then `test_social_flow`.
- **Step 5:** LinkedIn PDF (optional).
- **Step 6:** Slack report with the post link, guide URL, keyword, flow ID and test result.
- **Never:** post the same thing twice, create a second flow for one post, use one account-wide flow, send bulk DMs, or name competitors or the creators you track.

## Reels: hands-free, or your own video

- **Hands-free:** write the reel scripts in the tracker doc's Reels tab (`skills/organic-marketing-engine/references/tracker-doc.md`), then set a row to **Queued**. The 15:00 routine renders it with your approved avatar look and posts it (`reels-auto.md`). It needs avatar-tool API credit, so turn on auto-reload.
- **Your own video:** upload the .mp4 in **Settings → Vault** with "Keep original file", copy its public link, and post `🎬 Reel ready · <URL> · KEYWORD · <topic>` in your Slack self-DM. That line wins over the queue.

## Reports and alerts

- Every slot report starts "✅ <slot> done" and lists what was completed and what was skipped. A failed step never stops the rest.
- Platform errors go straight to your developer as a DM (tool, exact error, post link, workaround), at most once per error per day. Billing problems come to you.
- Prompt templates for all 6 routines: `skills/organic-marketing-engine/references/cloud-routine-templates.md`. Keep a copy of each live prompt in your private repo.

## Known limits

- The follow gate checks a typed word ("DONE"). A button version is planned.
- Numbers on posts under 24 hours old are early. The nightly report says so.
- Don't run two copies of the same slot (for example an old desktop task and a cloud routine), or you'll get double posts.
