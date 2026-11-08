# Agent rules (all playbooks, every agent)

These rules apply whenever Claude, ChatGPT, Grok or any other agent works on a platform account through this kit. Every skill in the kit follows them.

## 1. Always give exact, clickable links

Whenever the agent tells the user about something they can open, check or act on, it gives the **full URL as a clickable link**. Examples: a page it built, a form, a flow, a setting, a report, an ad, a guide.

- **Format:** a markdown link with a plain name, e.g. `[Your new lead form](https://…)`. Always start with `https://`.
- **Deepest page:** link straight to the exact page that does the job. Never write "go to the home page, then click…" when a direct URL exists.
- **One link per step:** in step-by-step instructions, every step that happens on a website has its own link.
- **After every build or change:** end with the links to what was created or changed, so the user can check it in one click. Examples: the guide page, the Social Flow, the pipeline, the workflow, the Meta campaign draft, the published Instagram post.
- **Use real links only:** take URLs from tool results (`url`, `public_url`, `permalink`, `app_url`, `editor_url`, `preview_url` and similar fields) or from pages the agent actually opened. **Never invent or guess a URL.**
- **When there's no URL:** say so plainly, name the screen ("Settings → App Store → Instagram in your account"), and link the closest page that does exist.
- **Never put secrets in a link:** no tokens, passwords, phone numbers or personal data in query strings.

### Common external pages
| What | Link |
|---|---|
| Meta Ads Manager | https://adsmanager.facebook.com/ |
| Meta Business settings (Pages, ad accounts, people) | https://business.facebook.com/settings |
| Meta Business Suite (inbox, posts, forms) | https://business.facebook.com/ |
| Claude connectors | https://claude.ai/settings/connectors |
| Composio (Instagram publishing connection) | https://app.composio.dev/ |
| This kit on GitHub | https://github.com/myappz-ai/agentic-business-kit |

For anything inside the user's platform account, use the link the tool returns for that item.

## 2. Approval before anything goes out
Paid ads, bulk messages and anything a customer sees go live only after the user's explicit "go ahead". The only exception is something the user has pre-authorized in writing, such as per-post Social Flows in the organic engine.

## 3. Facts only
Use only numbers and claims from tools or pages the agent actually opened. No income promises, fake discounts or invented testimonials.

## 4. Connection order: platform first, then official connectors, then Composio
When a job needs a tool, use the first option that can do it:
1. **The platform account connector.** CRM, pipelines, WhatsApp, email, calendar, forms, websites, Social Flow, invoices and ad drafts all live there. Always check it first.
2. **The agent's official connectors.** In Claude: Claude connectors (e.g. Meta Ads, Gmail, Google Drive, Slack, Canva). In ChatGPT: its apps/plugins.
3. **Composio, or any other connector the user already has.** Use it for whatever 1 and 2 can't do (e.g. Instagram carousel publishing, YouTube, GitHub).

If the user already works with Composio or another connector they prefer, go with it. Don't block, nag, or insist on switching; a working setup beats the "right" one.

**Teach as you go:** when you ask the user to connect something, say in one plain line what it's for and what it will let them do. The goal is that they understand their own setup, not just that it works.
