# Rendering and publishing (Composio)

## Workbench setup (each run; the sandbox can reset)
1. `COMPOSIO_SEARCH_TOOLS` with a new session (Instagram use case). Confirm that the active Instagram connection's username is the **brand handle**. If it isn't, stop and alert the owner. Never publish to the wrong account.
2. In `COMPOSIO_REMOTE_WORKBENCH`:
   - Font: if `/mnt/files/fonts/Figtree.ttf` is missing, download https://github.com/google/fonts/raw/main/ofl/figtree/Figtree%5Bwght%5D.ttf to that path.
   - Renderers: if `/mnt/files/renderer_v3_postcard.py` or `/mnt/files/renderer_v5_bigtype.py` is missing, write it from this skill's `references/` (paste the file contents).
   - Avatar: refresh `/mnt/files/photos/<handle>.jpg` from `INSTAGRAM_GET_USER_INFO` (`profile_picture_url`) every run, because the CDN link expires.

## Render
```python
exec(open('/mnt/files/renderer_v3_postcard.py').read())   # or renderer_v5_bigtype.py
paths = render(spec, '/mnt/files/ig_queue/<YYYY-MM-DD>_<keyword>')
problems = qa()          # must be [] - else shorten copy and re-render
```
Save the spec JSON and the caption text next to the slides.

## Upload and publish
1. Upload each slide with `upload_local_file` and keep each `s3key`.
2. Check today's media (`INSTAGRAM_GET_IG_USER_MEDIA`, limit 5) so this slot is never posted twice.
3. `INSTAGRAM_CREATE_CAROUSEL_CONTAINER`: `ig_user_id` = brand IG id, `caption`, `child_image_files` = `[{name, mimetype:"image/jpeg", s3key}]` in slide order.
4. Sleep (bash) until the slot time.
5. `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` with the creation_id.
6. `INSTAGRAM_GET_IG_MEDIA`: get the permalink and media_id.
7. On failure, retry **once** with a new container. Never publish twice.
8. **Immediately** create the Social Flow (`guide-and-flow-spec.md` §4).

## Video cover (optional, v5)
- Carousels accept video children.
- To use one, create each child with `INSTAGRAM_POST_IG_USER_MEDIA` (`is_carousel_item`) in order, then create the carousel with the `children` ids.

## Reels (talking-head video)
1. Use the final 9:16 .mp4 with the original colours. Don't brighten or re-grade it.
2. **Upload.** The Vault upload tool doesn't take video yet (see `known-issues.md`). Ask the owner to upload the file in the account's **Settings → Vault** and choose **Keep original file**. The other option re-encodes the video.
3. **Public link.** Open the file's preview in the Vault. The `<video>` source is the file's public link (strip any `#t=` suffix). Check it before using it: HTTP 200, `content-type: video/mp4`, and the same size as the local file.
4. `get_instagram_connection_health`, then check today's media so the slot is never posted twice.
5. Publish with `publish_instagram_post`: `video.url` = the public link, plus the caption (preview, then confirm). If it returns `container_id`, wait about 30 s and call again with only `container_id`.
   - Or use Composio: `INSTAGRAM_POST_IG_USER_MEDIA` (`video_url`, media_type REELS), then `INSTAGRAM_POST_IG_USER_MEDIA_PUBLISH` with `max_wait_seconds` 180.
6. **Immediately** create the Social Flow with the follow gate on (`guide-and-flow-spec.md` §4).

**Timing note (one account, not yet a rule):** on the account this was built on, reels posted 15:00–17:00 local time had the highest median reach (3,783 against 2,422 for late morning), and reels reached about 3× more people than carousels.
