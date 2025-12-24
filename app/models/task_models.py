from sqlmodel import SQLModel, Field,Relationship
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


class TaskBase(SQLModel):
    title: str
    description: str
    due_date: date|None=None
    status: Status
    priority: Priority
    user_id:int=Field(foreign_key="user.id")


class Task(TaskBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    owner:"User"=Relationship(back_populates="tasks")


class TaskResponse(TaskBase):
    id:int

class TaskCreate(TaskBase):
    pass


class TaskPatch(SQLModel):
    title: str|None=None
    description: str|None=None
    due_date: date|None=None
    status: Status|None=None
    priority: Priority|None=None
