from fastapi import APIRouter,Depends,Query
from sqlmodel import Session,select
from app.models.user_models import User,UserCreate
from app.core.database import get_session



users_router=APIRouter(prefix='/users',tags=['users'])

@users_router.get("/")
def get_user(session:Session=Depends(get_session)):
    db_users=session.exec(select(User)).all()
    return db_users

@users_router.post("/")
def create_user(user:UserCreate,session:Session=Depends(get_session)):
    db_user=User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user