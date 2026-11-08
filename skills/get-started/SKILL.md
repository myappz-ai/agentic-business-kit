---
name: get-started
description: The mandatory first-run setup for this kit. It connects the business account, syncs the business profile, checks every channel, fills the missing details, applies the house rules, marks setup as done, and recommends the first playbook. Use when someone says "get started", "set me up", "set up my account", "connect my account", or "I just installed this", and ALWAYS before any other playbook in this kit when setup is not marked done in the account.
---

# Get started

This is the front door of the kit. A new user knows only one sentence, "Get started", and leaves with a connected, checked account and their first playbook running. Speak in plain words, a few questions at a time, no jargon. Every step ends with clickable links (see `docs/AGENT_RULES.md`).

Setup is saved **in the business account**, not in the chat, so it carries over to every agent (Claude, ChatGPT or any other) and never has to be repeated.

## Step 1 – Is the account connected?
Call the account connector's `get_business_profile`.

**Connected:** say "Connected to <business name>." Ask the user to confirm that's the right business. If it isn't, stop: the wrong account is connected.

On a brand-new account the business name is often empty, or the account still has a placeholder name. Show the account name you see (`sub_account.name` from `get_business_profile`) and ask whether it's the right account. If it is, the business name saved in Step 3 is what customers see. If the user also wants the account itself renamed, use a rename tool when the platform provides one; otherwise tell them where the agency dashboard does it.

**Not connected:** the user has to add the connection once, in their agent's own settings. An agent cannot add a connection from a chat message. Give the steps for the agent you are running in:
- **Claude:** open [Claude connectors](https://claude.ai/settings/connectors) → **Add custom connector** → paste the account's connection link → **Add** → sign in if asked. Then start a new chat and say "Get started" again.
- **ChatGPT:** open [ChatGPT plugins](https://chatgpt.com/plugins) → **+** → **Add custom MCP server** → paste the connection link under *Connection* → create it as a plugin → install it → start a new chat, type **@** and pick it → say "Get started".
- **Any other agent:** open the agent's connectors / MCP settings, add a remote (HTTP) MCP server with the connection link, then come back.

Say where the connection link comes from: the user's account provider, or the account's AI-connection page. Then add:
> "Paste the link into your agent's connector settings, **not** into this chat. It can contain your access key."

If the user pastes a link containing a key into the chat anyway, don't repeat it. Tell them to rotate the key in their account once setup is done.

## Step 2 – Already set up?
Call `query_custom_values` with search `agentic_kit_setup`.
- **Found:** say "Your account is already set up (<date>)." Run Step 4 again quietly to catch anything that broke. If something broke, report it with fix links. Then go to Step 6.
- **Missing:** continue.

## Step 3 – About the business
Call `get_business_brief`. It returns what is known and the questions still open.

**Ask first for a source, not for answers:** "Share your website (or any page about your business) and I'll fill in everything I can." Read it and prefill the brief, the Business Profile and the logo from it. Use only what the page actually says. A Google Business share link may be blocked for agents; if it can't be read, say so and ask for the website or the business name and city instead.

**One go covers the whole setup.** When the user gives a source and asks you to set up (for example "set it up from my website"), that request is their yes: replace everything you found in one pass (profile, brief, logo), confirm each preview yourself, then show one table of what changed. Don't ask again field by field. Still ask before anything that sends to customers, publishes or costs money.

These are required before setup can finish:
- business name
- what the business does
- industry
- location / service area
- ideal customer
- contact details
- what a visitor should do first

Everything else is optional.

Ask only the missing questions, 2–3 at a time, in the user's words. Never invent answers. Save with `save_business_brief`: show the preview, then confirm only after the user's yes.

Also complete the **whole Business Profile**, not just the name. Call `get_business_profile` and walk every field the account's Business Profile screen shows:
- brand name, legal name, industry, business type, website
- business email, phone
- address (and the registered address, if the screen has a separate one), city, state, pincode, country
- timezone, base currency, allowed currencies
- tax id (GSTIN / PAN, or "business not registered")
- representative: name, role, email, phone

Fill what the user tells you with `update_business_profile`. Preview the brief and the profile together as one review table, and save both on one "yes". Don't trust the completeness score alone: re-read `get_business_profile` and list any field that is still empty. If a field can't be set through a tool, say so plainly and give the screen to finish it (Settings → Business Profile). Never leave the user thinking the profile is complete when it isn't.

Logo: offer it, but it's optional.
- If they have one, upload it: `get_logo_upload_url`, then PUT the file. If the upload link fails or expires, send it as `image_base64` (about 256×256 PNG) to `set_business_logo`.
- If they don't have one, offer a simple placeholder mark in their brand colours, and say they can replace it any time.
- Preview, then save on their yes.

## Step 4 – Check every channel
Run these read-only checks and show **one** table: Channel | Status ✅ / ⚠️ / ❌ | What it means | Fix (clickable link).

| Channel | Tool | Needed for |
|---|---|---|
| Instagram | `get_instagram_connection_health` | Organic marketing engine (comment-to-DM) |
| Meta ads | `get_ad_connection_health` | Lead-form ads |
| WhatsApp + email | `get_channel_readiness` | Instant replies and follow-ups |
| Calendar | `list_event_types` | Booking appointments |

Also call `query_integrations` (the account's App Store) and tell the user which connections are **required** and which are **optional**:

| Connection | Required? | Why |
|---|---|---|
| AI model | Required | Powers the assistant inside the account |
| Email sending (SMTP) | Required | Welcome emails, reminders, invoices |
| WhatsApp Business | Required in India | Instant replies and follow-ups to leads |
| Calendar / booking page | Required if customers book appointments | Bookings and reminders |
| Instagram / Meta | Required only for the marketing and ads playbooks | Comment-to-DM, lead-form ads |
| Zoom, Slack, Google, Canva and others | Optional | Add when a playbook needs them |

Connect required ones first. Use a tool that returns a connect link when the platform provides one; otherwise give the exact screen (Settings → App Store, or the channel's own screen) and re-check with the health tool after the user says it's done.

- Check in this order: the platform account first, then the agent's official connectors, then Composio or anything else the user already uses (`docs/AGENT_RULES.md` rule 4). If the user already has a working Composio connection for something, count it as ✅.
- For each ⚠️ / ❌, add one plain line on what that connection is for, so the user learns their setup.
- ❌ items don't block setup. They block only the playbooks that need them, so say which ones.
- Fixes happen in the user's own account, on its login screens. Never ask for passwords or codes.
- If a tool reports something odd (an empty or garbled field), report it plainly as a platform issue. Don't guess.

## Step 5 – Rules and done-marker
1. Tell the user the house rules in plain words, in four lines:
   - you'll always get clickable links
   - nothing goes to customers or costs money without your "go ahead"
   - only real facts and numbers
   - your account's name is the only brand your customers see
2. Mark setup as done in the account with `set_custom_value`: name `agentic_kit_setup`, value `done · v1 · <YYYY-MM-DD> · channels: <ready list>`, category `agentic-kit`. Preview first, then confirm on the user's yes.

## Step 6 – First playbook
Recommend **one** next step from the user's goal and the channel table, and offer to start it now:

| Goal | Ready channels | Say |
|---|---|---|
| More leads from Instagram, no ad budget | Instagram ✅ | "Setup my organic marketing engine" |
| Leads from ads | Meta ads ✅ + WhatsApp or email ✅ | "Launch lead form ads" |
| A channel that's needed is ❌ | — | Fix that first (link), then the playbook |

Finish with one summary:
- what's connected ✅
- what's waiting ⚠️ / ❌, with links
- the business brief, saved
- the one next step

## Rules that never change
- **Always give exact, clickable links** (see `docs/AGENT_RULES.md`).
- **This playbook is the gate.** No other playbook in the kit runs until `agentic_kit_setup` exists in the account.
- Never ask for, repeat or store passwords, keys or one-time codes in the chat.
- Never invent business details; use the user's words.
- Writes (brief, profile, logo, done-marker) are previewed first. One clear "go" from the user covers the whole setup pass; never ask field by field. Anything that sends, publishes or costs money still needs its own yes.
- Plain words. No file names, tool names or technical terms in what the user reads.

## Done when
- [ ] The account is connected, and the user confirmed it's the right business
- [ ] The required brief questions are answered and saved
- [ ] The channel table is shown, with fix links
- [ ] `agentic_kit_setup` is saved in the account
- [ ] The first playbook is recommended (and started, if the user said yes)
