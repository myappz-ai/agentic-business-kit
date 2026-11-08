# Known issues and workarounds (as of Nov 2026)

| Issue | Effect | Workaround | Permanent fix (platform) |
|---|---|---|---|
| Unattended scheduled runs are sometimes blocked by the session's safety check at the `create_social_flow` confirm step (flagged as an "account & standing-rule change"). | The post goes live without its flow, and commenters get nothing. | Quote the owner's authorization verbatim in every prompt. The backstop check (in an attended session) and the nightly sweep create any missing flow. | Add an optional `social_flow` object to `publish_instagram_post`: one preview, one confirm, and `flow_id` returned. Or make `create_social_flow` `apply_to:"next_post"` reliable. |
| `create_social_flow` sometimes returns Bad Gateway. | No flow is created. | Run `get_social_flow` first, then retry after 30, 90 and 180 s. | Retry logic on the server. |
| `create_short_link` fails ("is_active column of url_links"). | No short links. | Use full URLs with UTMs. | Fix the column. |
| Vault upload token lives about 60 s. | PDF uploads fail. | Build guides as web pages, not PDFs. | Longer token TTL. |
| Public guide URLs render client-side. | A plain HTTP fetch looks empty. | Verify with `get_page_html`. | Server-side render / meta. |
| The follow gate only accepts the typed word "done". There is no opt-in tap, existing followers are asked to follow again, and the "not followed yet" message can't be set. | Some people type "following" and never get the guide. | The follow-gate message says "reply DONE here". | Button gate: "Send me the link" opt-in, skip existing followers, "Visit Profile" + "I'm following ✓" buttons, re-check with an editable retry message, typed fallback words. |
| The Vault upload tool accepts only PDFs and images, and Vault tools return no public link for a file. | The agent can't upload a reel. | The owner uploads the .mp4 in Settings → Vault and picks **Keep original file**. The agent reads the video's public link from the Vault preview and checks it (see `publishing.md` → Reels). | Accept .mp4/.mov with a keep-original option, and return `public_url` for every Vault file. |
| On some accounts the Social Flow tools are only reachable through `nova_call_tool`. | A prompt that says "call create_social_flow directly" can't find the tool. | Call it through `nova_call_tool` with the same arguments. | Expose the Social Flow tools directly on every account. |
| Comments from the brand's own account never trigger flows. | Owner tests look broken. | Test from a second account, or DM the keyword. | — |
| Flows don't replay comments made before the flow existed. | Early commenters are missed. | Create the flow immediately after publishing. Ask early commenters to DM the keyword. | Backfill option. |
| Composio's sandbox can reset. | Renderer and font go missing. | The run recreates them from `references/`. | — |
| The platform's `create_form` adds no submit button (affects landing-page forms, not flows). | The hosted form has no Submit button. | Add it by hand in the Form builder, or use a native embed. | Always append a submit element. |
