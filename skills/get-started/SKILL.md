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

Logo: offer it, but it's optional (`set_business_logo`).

## Step 4 – Check every channel
Run these read-only checks and show **one** table: Channel | Status ✅ / ⚠️ / ❌ | What it means | Fix (clickable link).

| Channel | Tool | Needed for |
|---|---|---|
| Instagram | `get_instagram_connection_health` | Organic marketing engine (comment-to-DM) |
| Meta ads | `get_ad_connection_health` | Lead-form ads |
| WhatsApp + email | `get_channel_readiness` | Instant replies and follow-ups |
| Calendar | `list_event_types` | Booking appointments |

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
- Writes (brief, logo, done-marker) are previewed first and confirmed only after the user's yes.
- Plain words. No file names, tool names or technical terms in what the user reads.

## Done when
- [ ] The account is connected, and the user confirmed it's the right business
- [ ] The required brief questions are answered and saved
- [ ] The channel table is shown, with fix links
- [ ] `agentic_kit_setup` is saved in the account
- [ ] The first playbook is recommended (and started, if the user said yes)
