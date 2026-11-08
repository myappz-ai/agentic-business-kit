# Readiness audit – organic marketing engine

Run every check, in parallel where possible, and report one table: **Piece | Status (✅ / ⚠️ / ❌) | Evidence**. Save it to the brand's project as `<Brand>_IG_Engine_Readiness_<YYYY-MM-DD>.md`.

## Checks

| # | Piece | Tool (brand's sub-account connector unless noted) | Pass condition |
|---|---|---|---|
| 1 | Right sub-account | `get_business_profile` | Brand name matches the client. If not, stop: wrong connector. |
| 2 | Instagram connected | `get_instagram_connection_health` | Account listed, `status: connected` |
| 3 | DMs | same | `can.dms.ready: true` |
| 4 | Comment replies | same | `can.comment_replies.ready: true` |
| 5 | Publishing | same | `can.publishing.ready: true` |
| 6 | Token | same | `live.token_valid: true`; warn if `token_expires_in_days` < 14 |
| 7 | Webhooks | same | `subscribed_fields` includes comments, messages, messaging_postbacks (Instagram Login) |
| 8 | Existing flows | `list_social_flows` | Note any stale "any_comment" flows: they reply to every comment. Recommend pausing them. |
| 9 | Recent posts | `list_instagram_media` (limit 30) | Baseline: post types, which have flows, comment counts |
| 10 | Guides site | `query_sites` / `list_funnels` → `list_funnel_pages` | A "<Brand> Free Guides" site exists, or must be built in Phase 2 |
| 11 | Brand assets | `get_business_profile` | logo_url, brand colours. Ask the owner if missing. |
| 12 | Publisher (Composio) | `COMPOSIO_SEARCH_TOOLS` (Instagram use case) → `toolkit_connection_statuses` | An ACTIVE Instagram connection whose username = the brand handle |
| 13 | Reports channel | Slack connector | Can post to the owner's self-DM or the chosen channel |
| 14 | Baseline numbers | Composio `INSTAGRAM_GET_IG_USER_MEDIA` + `INSTAGRAM_GET_IG_MEDIA_INSIGHTS` (last 30) | Median reach, top 5 posts, and which posts asked for a comment keyword |

## Verdict

- **NOT READY** if 2, 3 or 12 fails. Tell the owner exactly what to do, in plain words:
  - Instagram: "In your SaaS Universe sub-account go to Settings → App Store → Instagram. Connect with **Instagram Login** and allow every permission. It must be a Business or Creator account."
  - Composio: "Add your brand's Instagram as a connection in Composio, so I can publish and read insights."
  - Stop here. Re-run the audit when they say it's done.
- **READY WITH WARNINGS** if only items 6, 8, 10, 11 or 13 are flagged. Continue and fix them in Phase 2.
- **READY** when every check passes.

## Common failures seen

- A Facebook-Page-linked Instagram whose token Meta rejects ("pages_… permission must be granted before impersonating a user's page"). Fix: reconnect via Instagram Login.
- Composio connected to the owner's *personal* account, not the brand's. Never publish until the username matches.
- An old "any comment" flow on a placeholder post (media id like "534"). Pause it.
