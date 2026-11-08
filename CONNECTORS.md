# Connectors

| Connector | Needed by | Used for | Check |
|---|---|---|---|
| Your platform account connector (MCP) | All playbooks | Guides site, Social Flows, CRM contacts, pipelines, workflows, templates, lead sync | `get_business_profile` returns your brand |
| Instagram (inside your platform account, Instagram Login) | Organic engine | Comment replies, DMs, webhooks | `get_instagram_connection_health`: DMs and publishing ready |
| Composio (Instagram toolkit) | Organic engine | Render slides, publish carousels, read insights | Its active Instagram connection username = your handle |
| Meta Ads MCP | Lead-form ads | Campaigns, ad sets, creatives, ads, previews, insights | `ads_get_ad_accounts` lists your ad account |
| Meta in your platform account (Ad Launcher → Platforms) | Lead-form ads | Lead-form sync into the CRM | `get_ad_connection_health` |
| WhatsApp Business (WABA) in your platform account | Lead-form ads | Instant reply and nurture | `list_waba_connections`: GREEN, display name approved |
| Email sender (SMTP) in your platform account | Lead-form ads | Instant confirmation email | `list_smtp_connections` |
| Slack | Optional | Reports and alerts | Can post to your chosen channel |
| Claude in Chrome | Optional | Building the instant form in Ads Manager | Browser tab opens |
