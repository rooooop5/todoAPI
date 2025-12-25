from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from app.core.database import get_session
from app.models.user_models import User,UserCreate,UserResponse
from app.core.security import encrypt_password,verify_password
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm


auth_router=APIRouter(prefix="/auth",tags=["auth"])
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")

@auth_router.get("/")
def default():
    return {"msg":"Created new auth route."}

@auth_router.post("/register",response_model=UserResponse,status_code=201)
def create_user(user:UserCreate,session:Session=Depends(get_session)):
    user.password=encrypt_password(user.password)
    db_user=User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@auth_router.post("/login")
def login(login_req:OAuth2PasswordRequestForm=Depends(),session:Session=Depends(get_session)):
    db_user=session.exec(select(User).where(User.username==login_req.username)).first()
    if not db_user:
        raise HTTPException(status_code=401,detail="Unauthorized access.")
    db_user.password
    if not verify_password(login_req.password,db_user.password):
        raise HTTPException(status_code=401,detail="Unauthorized access.")
    return {"access_token":db_user.username,"token_type":"bearer"}