from sqlmodel import SQLModel, Field
from datetime import date
from enum import Enum


# ------creating a class by inheriting Enum to for storing status of tasks------
class Status(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'


# ------creating a class by inherting Enum to store priority of tasks-------
class Priority(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    due_date: date|None=Field(default=None)
    status: Status
    priority: Priority
