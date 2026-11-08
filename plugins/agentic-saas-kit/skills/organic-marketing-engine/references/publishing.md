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
