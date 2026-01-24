# CRM System Implementation Plan

## Goal Description
Design and build a secure CRM system with a web interface. The system will handle customer data (located in `CRM Data/`) and enforce security by design principles.

## User Review Required
> [!NOTE]
> **Tech Stack**: 
> - **Frontend**: Next.js (React) - for a modern, responsive, and secure UI.
> - **Backend**: FastAPI (Python) - for high performance, automatic validation (Pydantic), and easy security integration.
> - **Database**: SQLite (dev) / PostgreSQL (prod).
> - **Security**: OAuth2 with JWT, BCrypt, Security Headers (Helmet/Next.config).

## Data Schema (Inferred from Files)
We will create database models based on these CSV files:
- **Accounts** (`accounts.csv`): Companies, sectors, revenue, employees.
- **Products** (`products.csv`): Product details and pricing.
- **Sales Pipeline** (`sales_pipeline.csv`): Opportunities, deal stages (Won/Lost/Engaging), values.
- **Sales Teams** (`sales_teams.csv`): Agents, managers, regional offices.

## Proposed Changes

### 1. Project Initialization
- Initialize `CRM Tool/frontend` (Next.js) and `CRM Tool/backend` (FastAPI).
- Create virtual environment and install dependencies.

### 2. Backend Development (`CRM Tool/backend`)
- **Models**: Create SQLAlchemy/SQLModel classes matching the CSV structure.
- **Ingestion Script**: Create `scripts/import_data.py` to read CSVs from `../../CRM Data` and populate the DB.
- **API**:
    - `POST /token`: Login endpoint.
    - `GET /dashboard`: Aggregate stats (Total Revenue, Deal Counts).
    - `GET /accounts`: List/Search accounts.
    - `GET /pipeline`: List opportunities.
- **Security**: Implement rate limiting, CORS configuration, and Input Validation.

### 3. Frontend Development (`CRM Tool/frontend`)
- **Dashboard**: Charts using Recharts/Chart.js showing Revenue trends and Pipeline stages.
- **Tables**: Data grids for Accounts and Pipeline with filtering/sorting.
- **Auth**: Login page with JWT storage (HttpOnly cookies or secure local storage pattern).

## Verification Plan

### Automated Tests
- Backend: Test data ingestion integrity and API security (auth enforcement).
- Frontend: Test component rendering and protected routes.

### Manual Verification
- Verify data in Dashboard matches CSV summaries.
- Test "Security by Design": Attempt SQL injection on search, verify XSS protection on inputs.
