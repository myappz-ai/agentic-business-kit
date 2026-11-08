# Adding a playbook

The kit grows only with flows that are **proven**. Ask Claude to "add this to the Agentic SaaS Kit" (or "add this to the Agentic SaaS Kit"); the `add-proven-playbook` skill walks through it.

## Proven means
- It ran for a real brand for 2+ weeks, or one full campaign cycle.
- There are real results from the tools (leads, CPL, replies, bookings, sales).
- It was repeated at least twice with the same steps.
- Its failures and workarounds are written down.

## Each playbook has
- `skills/<name>/SKILL.md`: trigger phrases; Intake → Audit → Build → Test → Launch → Report; "Rules that never change"; "Done when".
- Every skill follows `AGENT_RULES.md`. Its rules must include "always give exact, clickable links".
- `skills/<name>/references/`: SOPs, templates, prompts, code and known issues. No client ids, handles, emails or secrets.

## Versioning
- New playbook: minor bump (0.1.0 → 0.2.0). Fix or improvement: patch bump.
- Update `plugin.json`, `CHANGELOG.md` and the README table together.

## Playbooks in the pipeline (not yet proven)
- VSL funnel
- Live webinar / workshop funnel (registration → reminders → show-up → offer)
- WhatsApp broadcast re-engagement
- Searchy shop launch for sellers
- Review / reputation campaign
