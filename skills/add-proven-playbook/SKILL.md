---
name: add-proven-playbook
description: Packages a new, proven growth workflow into the Agentic Business Kit as its own skill, so clients can replicate it. Use when someone says "add this to the Agentic Business Kit", "turn this flow into a playbook for clients", "package what we did for <brand>", or "update the Agentic Business Kit".
---

# Add a proven playbook to the Agentic Business Kit

The kit only holds flows that have **worked for a real client**. Content can change per brand; the flow must be repeatable.

## 1. Check that it's proven
Ask for or find evidence of all of these, and stop if any is missing:
- It ran for at least one real brand for **at least 2 weeks**, or through one full campaign cycle.
- There are real numbers: leads, CPL, replies, bookings or sales, pulled from the tools, not estimates.
- The steps were repeated at least twice with the same result. A one-off success doesn't count.
- Known failures and their workarounds are written down.

## 2. Make it brand-agnostic
- Replace brand names, ids, handles, URLs and numbers with `<PLACEHOLDERS>`. Keep the real numbers only as an "Evidence" note.
- Name the tools by connector: "the brand's platform account connector", "Meta Ads MCP", "Composio Instagram". Never hard-code a specific client's MCP.
- No platform, agency or client brand names anywhere: say "platform account", "the brand", "the client". The kit is white-label.
- Keep the LOCKED rules (approvals, tone, facts, compliance) exactly as they were proven.

## 3. Write the skill
Create `skills/<kebab-name>/`:
- `SKILL.md`:
  - Frontmatter `name`, plus a third-person `description` with trigger phrases.
  - Body under ~1,500 words: Setup check (run get-started if `agentic_kit_setup` is missing) → Intake → Readiness audit → Build → Test → Launch → Report.
  - "Rules that never change" and a "Done when" checklist. The rules must start with "Always give exact, clickable links (see `docs/AGENT_RULES.md`)" and say which links to give after each step.
- `references/`: SOPs, templates, prompts, code, checklists and known issues.
- Write instructions **for Claude**: imperative, step by step, with the exact tool names.

## 4. Update the kit
- `README.md`: add one plain-words line to "What you can ask for". Keep the README non-technical.
- `docs/CONNECTORS.md`: add any new connector.
- `docs/CHANGELOG.md`: a new version line (minor bump for a new playbook, patch for fixes).
- `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: bump `version` to match.

## 5. Validate and ship
- Check that `plugin.json` is valid JSON with a kebab-case name, that every skill folder has a `SKILL.md` with frontmatter, and that no client ids or secrets remain (search for digits-only ids, `@handles` and emails).
- Zip the plugin root to `agentic-business-kit.plugin`, and also as a `.zip` for people who upload skills one by one.
- Deliver the file, and save a copy and the changelog to the project.
