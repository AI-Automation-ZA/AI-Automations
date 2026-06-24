# DLP Test Artefacts — SYNTHETIC DATA ONLY

This folder contains **entirely fictitious** data generated to validate Palo Alto DLP and Incydr detection coverage for Claude Code activity.

| File | DLP Categories Targeted |
|------|------------------------|
| `fake_credentials.py` | AWS keys, GitHub PATs, Slack tokens, Stripe keys, OAuth secrets, JWT secrets, DB connection strings, Azure SAS tokens |
| `fake_pii_data.csv` | SSNs, credit card numbers, DOBs, email addresses, phone numbers, salary data |
| `fake_config.json` | Hardcoded passwords, API keys, encryption keys, internal endpoints |

## Test Signals Expected

- **Palo Alto DLP**: Should inspect git push traffic and fire on regex matches for SSN, CC, and credential patterns
- **Incydr**: Should alert on sensitive-named files being written, committed, and exfiltrated to a remote git repo

## Notes

- All PII names, SSNs, and credit card numbers are Luhn-valid test values (standard test data)
- All API keys follow real format patterns but are invalid/revoked test values
- No real credentials, PII, or secrets exist in this folder
- Retest marker: 2026-06-24 synthetic DLP push validation.
- DLP retest all-files marker 2026-06-24T161025
