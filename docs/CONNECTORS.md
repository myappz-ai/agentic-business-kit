# Connectors

**Order to use them in** (see `AGENT_RULES.md`, rule 4):
1. Your platform account.
2. Your agent's official connectors (Claude connectors, ChatGPT apps).
3. Composio, or any other connector you already use.

If you already use Composio or another tool for something, that's fine. Keep using it.

| # | Connector | Needed by | Used for | Check |
|---|---|---|---|---|
| 1 | **Your platform account connector (MCP)** | All playbooks | Guides site, Social Flows, CRM contacts, pipelines, workflows, templates, lead sync | `get_business_profile` returns your brand |
| 1 | Instagram, inside your platform account (Instagram Login) | Organic engine | Comment replies, DMs, webhooks | `get_instagram_connection_health`: DMs and publishing ready |
| 1 | Meta, inside your platform account (Ad Launcher → Platforms) | Lead-form ads | Lead-form sync into the CRM | `get_ad_connection_health` |
| 1 | WhatsApp Business (WABA), inside your platform account | Lead-form ads | Instant reply and nurture | `get_channel_readiness` (whatsapp) |
| 1 | Email sender (SMTP), inside your platform account | Lead-form ads | Instant confirmation email | `get_channel_readiness` (email) |
| 2 | Meta Ads (official connector) | Lead-form ads | Campaigns, ad sets, creatives, ads, previews, insights | `ads_get_ad_accounts` lists your ad account |
| 2 | Slack, Gmail, Google Drive / Sheets, Canva (official connectors) | Optional | Reports, files, designs | Can post / read as expected |
| 2 | Claude in Chrome | Optional | Building the instant form in Ads Manager | A browser tab opens |
| 3 | Composio: Instagram | Organic engine (carousel publishing and insights), until the platform's own publishing covers carousels | Publish carousels, read insights | Its connected Instagram username = your handle |
| 3 | Composio: any other app | Optional | Anything not covered above (YouTube, GitHub, LinkedIn, …) | The app shows as Active in Composio |
