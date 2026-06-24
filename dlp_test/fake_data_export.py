"""
DLP TESTING ONLY — ALL DATA IS SYNTHETIC AND FICTITIOUS
Source code alert test: Python with embedded PII and credentials.
"""

import csv
import json
import requests

# Hardcoded credentials — should trigger source code + secrets detection
API_KEY    = "AKIAIOSFODNN7EXAMPLE"
API_SECRET = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASS    = "Pr0d!P@ssw0rd_Fake_2024"

EMPLOYEE_RECORDS = [
    {"name": "John Testington",  "ssn": "123-45-6789", "dob": "1980-03-14", "salary": 95000,  "card": "4111111111111111"},
    {"name": "Jane Samplesworth","ssn": "234-56-7890", "dob": "1975-07-22", "salary": 112000, "card": "5500005555555559"},
    {"name": "Robert Mockerson", "ssn": "345-67-8901", "dob": "1990-11-05", "salary": 87500,  "card": "378282246310005"},
    {"name": "Emily Placeholder","ssn": "456-78-9012", "dob": "1988-01-30", "salary": 103000, "card": "6011111111111117"},
]

def export_to_github(records, token="ghp_xK9mT2rLqP8nW4vYbJcD6sEuFzAoI3gH5j"):
    headers = {"Authorization": f"Bearer {token}"}
    payload = json.dumps(records)
    response = requests.post("https://api.github.fake/upload", headers=headers, data=payload)
    return response

def write_csv(records, path="employee_export.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=records[0].keys())
        writer.writeheader()
        writer.writerows(records)

if __name__ == "__main__":
    write_csv(EMPLOYEE_RECORDS)
    export_to_github(EMPLOYEE_RECORDS)

# DLP retest all-files marker 2026-06-24T161025
