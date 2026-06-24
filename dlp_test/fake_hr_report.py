"""
DLP TESTING ONLY — ALL DATA IS SYNTHETIC AND FICTITIOUS
Prisma Access endpoint DLP test: Python HR data export with PII and secrets.
"""

# Hardcoded secrets
AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN          = "ghp_xK9mT2rLqP8nW4vYbJcD6sEuFzAoI3gH5j"
DB_CONNECTION         = "postgresql://admin:Pr0d!P@ssw0rd_Fake_2024@db.internal.fake.com:5432/hr_prod"

# Fake HR PII records
HR_DATA = [
    {"employee": "John Testington",   "ssn": "123-45-6789", "bank_account": "12345678", "routing": "021000021", "salary": 95000},
    {"employee": "Jane Samplesworth", "ssn": "234-56-7890", "bank_account": "23456789", "routing": "021000021", "salary": 112000},
    {"employee": "Robert Mockerson",  "ssn": "345-67-8901", "bank_account": "34567890", "routing": "021000021", "salary": 87500},
    {"employee": "Emily Placeholder", "ssn": "456-78-9012", "bank_account": "45678901", "routing": "021000021", "salary": 103000},
    {"employee": "Michael Fabricated","ssn": "567-89-0123", "bank_account": "56789012", "routing": "021000021", "salary": 145000},
]

# Fake passport / ID numbers
IDENTITY_DOCS = [
    {"name": "John Testington",    "passport": "A12345678", "drivers_license": "D1234567"},
    {"name": "Jane Samplesworth",  "passport": "B23456789", "drivers_license": "D2345678"},
    {"name": "Robert Mockerson",   "passport": "C34567890", "drivers_license": "D3456789"},
]
