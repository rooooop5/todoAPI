# Task Management API

A REST-style Task Management API built using FastAPI and SQLModel.

This project is a learning-focused backend API exploring:
- REST conventions
- FastAPI routing & dependency injection
- SQLModel ORM usage
- Validation & error handling

## Tech Stack
- FastAPI
- SQLModel
- PostgreSQL
- Uvicorn

## Status
🚧 Actively evolving — see CURRENT_IMPROVEMENTS.md

## Planned Extension/Follow-up project
Authentication and authorization are intentionally out of scope for this repository.

This project focuses on core REST API design, data modeling, and clean separation of concerns.

A follow-up project will extend this API with:

- JWT-based authentication

- Role-based access control

- Secure task ownership enforcement

The authenticated version will be developed as a downstream project in a separate repository to keep concerns isolated.

## Run Locally
```bash
git clone <repo-url>
cd task-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
