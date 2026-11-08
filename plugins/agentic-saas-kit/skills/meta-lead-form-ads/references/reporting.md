# Reporting and optimisation

## Daily report (schedule with `create_trigger`; read-only; morning + evening)
1. Meta (`ads_get_ad_entities` with insights): spend, leads, CPL, CTR, CPM and frequency, by campaign, ad set and ad, for yesterday and the last 7 days.
2. CRM (the client's sub-account):
   - leads that actually arrived (`list_ad_leads` / `query_contacts` by campaign tag)
   - contacted %, qualified %, meetings booked, won (`query_opportunities`)
   - payments (`query_transactions`) where relevant
3. **Cost per real lead** = spend ÷ CRM leads. Trust the CRM over the pixel; pixel lead events can double-fire.
4. Classify each ad set or ad as **GOOD / HOLD / JUNK**. Write a RED list and **one main flag**. Evidence over summaries.

## RED flags
- An ad above the client's CPL ceiling (default 3× target CPL), or 3× target CPL spent with 0 leads.
- Leads arriving but the contacted % under 60 within 24 h. This is a sales-process problem, not an ads problem.
- CTR falling and frequency above 2.5. That's creative fatigue: refresh the creatives.
- Leads not reaching the CRM. Check the form sync immediately.

## Rules
- Recommend, don't execute. Pausing, budget changes and new creatives need the owner's yes.
- When the owner asks for cleanup: pause what has high CPL **and** no qualified leads or sales. Keep anything that produces meetings or sales, even if its CPL is higher.
- Never pause a video ad without an explicit yes for that ad.
- Judge only after meaningful spend; RED flags can be raised earlier.
- Log every change: `date | brand | account | change | ids | approved by`.
