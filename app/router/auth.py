from fastapi import APIRouter,Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.user_models import User,UserCreate,UserResponse
from app.core.security import crypt_context
import bcrypt


auth_router=APIRouter(prefix="/auth",tags=["auth"])

@auth_router.get("/")
def default():
    return {"msg":"Created new auth route."}

@auth_router.post("/register",response_model=UserResponse,status_code=201)
def create_user(user:UserCreate,session:Session=Depends(get_session)):
    hashed_passwd=crypt_context.hash(user.password)
    user.password=hashed_passwd
    db_user=User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user