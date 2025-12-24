## Overview
A RESTful Task Management API built with FastAPI and SQLModel.
Supports users, tasks, filtering, and partial updates.

## Core Concepts
- Users can own multiple tasks
- Tasks can be accessed independently or filtered by user
- PATCH supports partial updates
- Authentication is intentionally out of scope

## User Endpoints
- GET    /users                # List users
- GET    /users/{id}           # Get user details
- GET    /users/{id}/tasks     # List tasks for a user
- POST   /users                # Create user

## Task Endpoints
- GET    /tasks                # List tasks (filterable)
- GET    /tasks/{id}           # Get task
- POST   /tasks                # Create task
- PUT    /tasks/{id}           # Replace task
- PATCH  /tasks/{id}           # Partial update
- DELETE /tasks/{id}           # Delete task

## Filtering
Tasks can be filtered using query parameters:
- status
- priority
- due_date

## Error Handling
- 404 when resource does not exist
- 422 for validation errors
- 409 for request conflict
- Custom error response format
- Centralized exception handler

## Database Design
- One-to-many relationship between User and Task
- Foreign key constraints enforced at DB level
- Indexed fields for username and email

## Authentication
Authentication and authorization are intentionally excluded.
A follow-up project will add JWT-based auth.
