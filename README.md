# Secure CRM Portal & Analytics

A modern, high-performance Customer Relationship Management (CRM) system built with **FastAPI** and **Next.js**, designed with a **Security by Design** philosophy.

## 🚀 Overview
This tool provides a premium interface for managing customer accounts, sales pipelines, and products. It ingests complex business data and presents it through a real-time, responsive dashboard.

## 🛡️ Security Architecture
We believe in transparency without compromise. This project implements the following security layers:

- **JWT Auth**: Stateless authentication using JSON Web Tokens with configurable expiration.
- **Bcrypt Hashing**: Industry-standard cryptographic hashing for all stored credentials.
- **CORS Mitigation**: Strict origin-filtering to prevent Cross-Site scripting and unauthorized API access.
- **Schema Validation**: Robust type-checking and input sanitization via Pydantic and TypeScript.
- **Environment Isolation**: Sensitive configuration is decoupled from the codebase using `.env` management.

> [!IMPORTANT]
> **Privacy Note**: To maintain the security of your deployment, never commit `.env` files. Use the provided `.env.example` templates to configure your environment safely.

## 🏗️ Tech Stack
- **Frontend**: Next.js 15, Tailwind CSS, Lucide Icons, Axios.
- **Backend**: FastAPI (Python), SQLModel, SQLAlchemy, SQLite.
- **Data**: Automated ingestion from multi-dimensional CSV sources.

## 🚦 Getting Started
To launch the system, please refer to the [Launch Guide](.agent/workflows/launch-crm.md).

1.  **Backend**: `cd "CRM Tool/backend" && uvicorn main:app --reload`
2.  **Frontend**: `cd "CRM Tool/frontend" && npm run dev`

---
*Developed with a focus on Security, Performance, and Visual Excellence.*