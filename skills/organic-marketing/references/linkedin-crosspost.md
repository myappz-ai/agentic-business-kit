# LinkedIn cross-post – PDF document posts

Every Instagram carousel also goes to LinkedIn, the same day, as **one PDF document post**. People can page through it and save it. Never post the slides as single images.

## Needs
- LinkedIn connected for the owner's profile (Composio LinkedIn, or the platform's own LinkedIn connection when it has one).
- The owner's authorization covers LinkedIn by name, quoted in each scheduled prompt.

## Steps
1. **Build the PDF** from the same rendered slides, in order, at 1080×1350:
   `ims[0].save(buf, format="PDF", save_all=True, append_images=ims[1:], resolution=150)` (Pillow).
2. **Find the author**: the owner's person URN (`urn:li:person:<id>`) from the LinkedIn connection.
3. **Upload the document** (LinkedIn REST, headers `LinkedIn-Version: <current YYYYMM>` and `X-Restli-Protocol-Version: 2.0.0`; if a version returns 426, use a newer month):
   - `POST /rest/documents?action=initializeUpload` with `{"initializeUploadRequest":{"owner":"<person URN>"}}`
   - `PUT` the PDF bytes to the returned `uploadUrl`
4. **Create the post**: `POST /rest/posts` with `author`, `commentary`, `visibility: PUBLIC`, `distribution.feedDistribution: MAIN_FEED`, `lifecycleState: PUBLISHED` and `content.media {title, id: <document URN>}`.
   - Commentary is "little text": backslash-escape `( ) [ ] { } < > @ | ~ _ * \`, or the post breaks.
5. **Caption**: hook; "Free <doc> on page 4. Comment KEYWORD and I'll send it to you."; 3 value lines; a Source line when facts are used; 3 hashtags.
6. **Link** it in the report: `https://www.linkedin.com/feed/update/<post URN>/`.

## Replying to comments
- LinkedIn has no automated comment-to-DM. Reply **in the comment thread** with the resource link, once per person: "Here you go, <first name>: <link>".
- Reading comments through the API needs LinkedIn's Community Management access. Without it, read the LinkedIn notification emails (Gmail or the inbox connector) for new comments on the post, then reply.
- If you cannot read or reply, say so in the report and list the post so the owner can reply by hand. Never guess who commented.

## Rules
- Same slides, same keyword and same resource as the Instagram post.
- Never post the same carousel to LinkedIn twice. Check the profile's recent posts first.
- Kind tone and facts only, as on Instagram.
