from fastapi import APIRouter,Depends,Query
from sqlmodel import Session,select
from app.models.user_models import User,UserCreate,UserResponse
from app.core.database import get_session



users_router=APIRouter(prefix='/users',tags=['users'])

@users_router.get("/",response_model=UserResponse)
def get_user(session:Session=Depends(get_session)):
    db_users=session.exec(select(User)).all()
    return db_users

@users_router.get("/{user_id}",response_model=UserResponse)
def get_user_tasks(user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    return db_user
@users_router.get("/{user_id}/tasks")
def get_user_tasks(user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    usr_tasks=db_user.tasks
    return usr_tasks

@users_router.post("/")
def create_user(user:UserCreate,session:Session=Depends(get_session)):
    db_user=User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user