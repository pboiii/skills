# Security and Privacy

Goal packets can capture sensitive context. Treat generated files, logs, screenshots, traces, and proof artifacts as potentially private.

## Do not include

- API keys, secrets, tokens, cookies, session IDs, passwords, or `.env` values.
- Customer data, production records, private docs, unreleased plans, or regulated data.
- Browser tabs, notifications, emails, personal files, internal dashboards, or unrelated desktop content in screenshots.
- Production database dumps or destructive migration output unless explicitly approved and handled privately.

## Recommended proof handling

- Save proof under the goal folder's `proof/` directory.
- Redact or crop screenshots before committing or sharing.
- Keep sensitive proof local and add it to `.gitignore` when needed.
- Summarize sensitive evidence without exposing raw values.
- Review `proof/README.md`, logs, and screenshots before opening PRs or publishing artifacts.

## Permission gates

Require explicit authorization or documented repo policy before:

- pushing branches or opening PRs
- deploying or publishing packages
- writing to production systems
- deleting or migrating data
- changing billing, emails, notifications, or external sends
- adding dependencies or changing lockfiles for reasons outside the approved objective
