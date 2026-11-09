# Hands-free reels (cloud, no filming)

The afternoon slot can make its own talking-head reel every day: a script from the series doc → an AI avatar render → Instagram → the per-post Social Flow → LinkedIn and YouTube Shorts → the tracker doc → the report. The owner records nothing.

## Needs
- An AI avatar video tool connected through Composio (HeyGen today), with **API credit** (its API wallet is separate from the app plan). Turn on auto-reload, or the nightly report warns when the balance is low.
- The owner's avatar, and a list of **approved looks** saved in the LOCKED doc (look IDs plus a one-line description). Also list the looks that must never be used. The agent never picks a look outside the approved list.
- The tracker doc (`tracker-doc.md`) with a Reels tab, or the owner's queue.

## Which reel today
1. **Manual override first.** If the owner posted `🎬 Reel ready · <video URL> · KEYWORD · <topic>` in the reports channel in the last 14 days and it isn't posted yet, use that video.
2. **Otherwise, the series doc.** Take the lowest-numbered row whose Status is **Queued** and whose Date is today or earlier. Only one reel a day.
   - Script = that reel's spoken lines, word for word. Leave out "Screen:" notes and [placeholders]. A script with placeholders is not ready, so take the next row.
   - Look = the row's Look column (approved list only).
   - Keyword = the word before "→" in the row's "Keyword → gift" cell.
3. **Otherwise, write one.** 30–45 s, 90–120 words. Line 1 = the cost of the old way or a pain question. Then one named feature with a concrete result, then 2–3 steps. The CTA is 2 lines max and names the gift with a number.
4. If no look is set, rotate the approved looks by day of year.

## Render
- `POST /v2/video/generate` with `caption: true`, `dimension: {width:1080, height:1920}`, the avatar look and its default voice, and the script as `input_text`.
- Poll the status every 20 s for up to 25 min. Use `video_url_caption` when present, otherwise `video_url`.
- **Never brighten, re-grade or re-encode** the video. Owners notice.
- On a credit error or any render error, go to the fallback. Billing problems go in the owner's report, not to the developers.

## Publish
- Build the guide first (`guide-and-flow-spec.md`): it must deliver exactly what the CTA promises (same title, same number of points, steps or prompts).
- Sleep until the slot time, then publish the reel. If the platform's publish tool rejects a non-Vault video URL, use the Instagram Graph API through Composio: `POST /<ig-user-id>/media {media_type:"REELS", video_url, caption, share_to_feed:true}`, poll `status_code` until `FINISHED`, then `POST /<ig-user-id>/media_publish {creation_id}`. Instagram accepts the avatar tool's video URL directly.
- Caption: the hook, 3 short value lines, "Comment KEYWORD 👇", 3–5 hashtags.
- Create the Social Flow straight away, with the follow gate on, and test it.
- Cross-post per `reel-crosspost.md`. This replaces the LinkedIn PDF for reels.
- Update the reel's tracker row: Status **Posted**, Links, and Report "posted <date> · numbers tonight".

## Fallback
The slot is never empty. If the render or publish fails, post a cream big-type carousel (v5) on the same topic and say why in the report.

## Styles
The cloud render is a plain talking head with captions. Styled edits (split cards, tier boards, title bars) need an editor pass, so the report notes "style: plain (cloud)". The styles are listed in `reel-styles.md`.
