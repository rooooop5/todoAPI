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

## Run Locally
```bash
git clone <repo-url>
cd task-api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
