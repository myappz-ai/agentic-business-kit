# Reel cross-post: Instagram + LinkedIn + YouTube Shorts

Every reel goes to all three on the same day. The owner's standing authorization should name LinkedIn and YouTube, for example: "Whenever we create a reel, post it on Instagram, LinkedIn and YouTube at the same time."

1. **Instagram first**, with its Social Flow and follow gate.
2. **LinkedIn** (Composio LinkedIn): `LINKEDIN_UPLOAD_VIDEO {video_url}` → `LINKEDIN_CREATE_VIDEO_POST` → `LINKEDIN_CREATE_COMMENT_ON_POST {target_urn, object, actor: <owner person URN>, message: {text}}`. Put the guide link in that **first comment**.
3. **YouTube Shorts** (Composio YouTube): in the Composio workbench, download the mp4, `upload_local_file` it, then call `YOUTUBE_MULTIPART_UPLOAD_VIDEO` **once**. Use a title with "#Shorts", category 27 (Education), public, and the guide link in the description. Then add a comment with the link. The API can't pin it.
4. Keep "Comment KEYWORD" in the caption, but put the link where people can see it. Neither platform has automated DMs.

## Rules
- Check for a duplicate before uploading: look at the channel's last 10 uploads and the profile's recent posts.
- A cross-post failure never blocks the slot. Report "⚠️ <platform> pending" and let the nightly report retry.
- YouTube 429 "Video Uploads per day" comes from Composio's shared Google project. It resets at midnight Pacific. Don't loop; retry in the nightly run.
- Avatar-tool video links expire (about 7 days). For a late retry, get a fresh link from the render's status.
