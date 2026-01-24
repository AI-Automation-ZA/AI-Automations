# CRM Tool Backend Walkthrough

The backend for the CRM Tool is now fully operational, implementing **Security by Design** principles and a robust data layer.

## Achievements
- [x] **Secure API**: Implemented FastAPI with OAuth2 and JWT authentication.
- [x] **Data Ingestion**: Processed 8,000+ fictitious sales records and company data from CSV into a local SQLite database.
- [x] **Automated Verification**: Created and passed a verification suite (`verify_api.py`) testing security and data integrity.

## Key Components

### 1. Security (Security by Design)
- **Authentication**: JWT-based tokens with expiration.
- **Hashing**: Secure password hashing using `pbkdf2_sha256`.
- **CORS**: Configured to restrict access to trusted origins.
- **Protection**: All data-sensitive endpoints (Dashboard, Accounts, Pipeline) require a valid token.

### 2. Data Layer
- **Models**: SQLModel/SQLAlchemy used for type-safe database interactions.
- **Database**: Ported from CSVs to relational SQLite:
    - `Account`: 85 companies.
    - `Product`: 7 products with pricing.
    - `SalesPipeline`: ~8,800 opportunities.
    - `SalesTeam`: 35 agents and managers.

## How to Run & Verify
1.  **Environment**: Activate `.\venv\Scripts\activate` (Windows).
2.  **Start API**: `uvicorn main:app --reload` in `CRM Tool/backend`.
3.  **Default User**: 
    - Username: `admin`
    - Password: `admin123`

### Verification Results
```bash
Testing unauthorized access to /dashboard...
SUCCESS: 401 Unauthorized as expected.
Testing login with admin user...
SUCCESS: Logined in!
Testing /dashboard with token...
SUCCESS: Dashboard stats: {
  "total_accounts": 85,
  "total_products": 7,
  "total_revenue_won": 19688537.0,
  "total_deals_engaging": 2244
}
Testing /accounts with token...
SUCCESS: Received 5 accounts.
Testing /pipeline with token...
SUCCESS: Received 5 pipeline items.

ALL VERIFICATION TESTS PASSED!
```

## Current Blocker
- **Node.js Missing**: Cannot initialize the Next.js frontend until Node.js is installed on the host system.
