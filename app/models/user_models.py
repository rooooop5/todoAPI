from sqlmodel import SQLModel,Field,Relationship
from typing import Optional

class UserBase(SQLModel):
    username:str=Field(index=True,unique=True)
    email:str=Field(index=True,unique=True)
    hashed_passwd:str

class User(UserBase,table=True):
    id:int|None=Field(default=None,primary_key=True)
    tasks:Optional[list["Task"]]=Relationship(back_populates="owner")