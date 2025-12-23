# Task Storage API Project Requirements

## Project Overview

The goal of this project is to design and implement a RESTful API to manage tasks. The API will allow users to create, edit, delete, and retrieve tasks by their ID, due date, or other criteria. The application will use PostgreSQL as the database, SQLModel for ORM (Object-Relational Mapping), and Pydantic for data validation and serialization.

---

## 1. API Endpoints

### 1.1 Create Task  
**POST** `/tasks/`  
- **Description**: Creates a new task.
- **Request Body**: Task title, description, due date, status, and priority.
- **Response**: Returns the created task with an assigned ID.

---

### 1.2 Edit Task  
**PUT** `/tasks/{id}/`  
- **Description**: Updates an existing task.
- **Path Parameter**: `id`
- **Request Body**: Updated task fields.
- **Response**: Returns the updated task.

---

### 1.3 Delete Task  
**DELETE** `/tasks/{id}/`  
- **Description**: Deletes a task by ID.
- **Path Parameter**: `id`
- **Response**: Success response or error if the task does not exist.

---

### 1.4 Get Task by ID  
**GET** `/tasks/{id}/`  
- **Description**: Retrieves a task by its ID.
- **Path Parameter**: `id`
- **Response**: Returns the task.

---

### 1.5 Get Tasks by Due Date  
**GET** `/tasks/due/`  
- **Description**: Retrieves tasks that are due on a specific date.
- **Query Parameter**:
  - `due_date` — in `YYYY-MM-DD` format; if omitted, returns all tasks.
- **Response**: A list of tasks due on that date.

---

### 1.6 Get Overdue Tasks  
**GET** `/tasks/overdue/`  
- **Description**: Retrieves all tasks that are past their due date.
- **Behavior**:
  - A task is considered overdue if:
    - It has a `due_date` value, **and**
    - `due_date < current date/time`, **and**
    - The task status is not `completed`.
- **Response**: A list of overdue tasks.
- **Notes**:
  - The comparison must use the server’s current date/time.
  - Tasks without a due date should not be included.

---

### 1.7 Get All Tasks  
**GET** `/tasks/`  
- **Description**: Retrieves all tasks with optional filtering.
- **Query Parameters**:
  - `status` — filter by task status.
  - `priority` — filter by priority.
- **Response**: A list of tasks.

---

## 2. Technologies Used

- **Database**: PostgreSQL  
- **ORM**: SQLModel  
- **Validation**: Pydantic  
- **Web Framework**: FastAPI  

---

## 3. Development Guidelines

- Use RESTful conventions and meaningful HTTP status codes.
- Validate all input fields.
- Provide consistent response formats and helpful error messages.
- Handle edge cases:
  - Task not found  
  - Invalid date formats  
  - Invalid status/priority values  
- Include documentation for setup and usage.
- Include automated tests for all endpoints.

---
