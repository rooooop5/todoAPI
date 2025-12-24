from sqlmodel import SQLModel,Field,Relationship
from typing import Optional,TYPE_CHECKING

if TYPE_CHECKING:
    from .task_models import Task
class UserBase(SQLModel):
    username:str=Field(index=True,unique=True)
    email:str=Field(index=True,unique=True)

class User(UserBase,table=True):
    id:int|None=Field(default=None,primary_key=True)
    tasks:Optional[list[Task]]=Relationship(back_populates="owner")

class UserCreate(UserBase):
    pass

class UserResponse(SQLModel):
    id:int
    username:str
    email:str

class UserPatch(SQLModel):
    username:str|None=None
    email:str|None=None
