# Cloud routine templates

Six Claude Code cloud routines run the engine with the laptop closed. Fill the `{{…}}` placeholders, attach the connectors (the platform account, Composio, Slack or the reports channel, Apify, and the doc tool) and set cron in UTC. Every prompt starts with: "This run is unattended: never ask questions and never wait for a reply."

| Routine | Brand time | Prompt core |
|---|---|---|
| Viral watch | 06:15 | Read `creators.json`. Scrape each account's last 12 posts (Apify). A post is viral at ≥{{LIKES}} likes or ≥{{COMMENTS}} comments (likes -1 = hidden, so use comments). Skip anything reported in the last 7 days. For up to 5 that fit the audience, give the hook, why it worked, and an ORIGINAL version (hook, keyword, slot). Never put creator names in our content. One message to {{REPORTS}}. |
| News picks | 06:35 | Official news pages only, last 48 h. Keep only what the audience can use now. Up to 3 picks with a hook, keyword, angle and slot, no repeats. One message to {{REPORTS}}. |
| Morning carousel | 08:00 | Fetch `AUTOPILOT.md` from {{REPO}} and follow it: Step 0 topic → hook → guide → render, sleep, publish → Social Flow + follow gate + test → LinkedIn PDF → tracker row (Carousels, slot "8 AM") → report starting "✅ 8 AM done". |
| Reel | 15:00 | As `reels-auto.md`: override → series doc → write. Then render, guide, publish, flow, cross-post (`reel-crosspost.md`), tracker row → Posted, report "✅ 3 PM reel done". Carousel fallback. |
| Evening carousel | 20:00 | Same as the morning carousel, with the story/lesson pillar, slot "8 PM". |
| Nightly report | 23:30 | Insights for today's posts, safety net (missing flow or follow gate), cross-post catch-up, tracker update (`tracker-doc.md`), baseline medians, account watch (avatar-tool credit), then one report with a table, best/worst post and one change for tomorrow. |

## Always in every slot prompt
- The owner's **standing authorization, quoted word for word with its date.** Without it, an unattended run stops at the confirm step.
- **Developer alerts:** when a platform tool fails (tool error, follow gate, flow test failing twice), DM {{DEVELOPER}} at once with the tool, the exact error, the post link and the workaround. At most one alert per error per day. Billing goes to the owner, not the developer.
- **"Keep going and report what's done":** a failure in one step never stops the rest, and the report says what was skipped.
- Files come from a private repo through `COMPOSIO_PROXY_EXECUTE` (toolkit `github`). The routine never commits.

## Keep a copy
Keep each routine's live prompt in the owner's private repo (`routines/NN-name.md`, with the routine ID, cron and connectors). Update it whenever the routine changes.
