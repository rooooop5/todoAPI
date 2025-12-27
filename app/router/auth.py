from fastapi import APIRouter,Depends,HTTPException
from sqlmodel import Session,select
from app.core.database import get_session
from app.models.user_models import User,UserCreate,UserResponse
from app.core.security import encrypt_password,verify_password,SECRET_KEY,ALGORITHM,ACCESS_TOEKEN_EXPERATION_MINS,Token,TokenData,create_access_token
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from datetime import timedelta



auth_router=APIRouter(prefix="/auth",tags=["auth"])
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/token")
def get_user(token=Depends(oauth2_scheme),session:Session=Depends(get_session)):
    credentials_exception=HTTPException(status_code=401,detail="Cannot authorize user.")
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        username=payload.get("sub")
        if not username:
            raise credentials_exception
        token_data=TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    db_user=session.exec(select(User).where(User.username==username)).first()
    if not db_user:
        raise credentials_exception
    return db_user

    



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

@auth_router.post("/token",response_model=Token,summary="Route Login Access Token Post")
def login(login_req:OAuth2PasswordRequestForm=Depends(),session:Session=Depends(get_session))->Token:
    db_user=session.exec(select(User).where(User.username==login_req.username)).first()
    if not db_user:
        raise HTTPException(status_code=401,detail="Unauthorized access.")
    if not verify_password(login_req.password,db_user.password):
        raise HTTPException(status_code=401,detail="Unauthorized access.")
    expiry_period=timedelta(minutes=ACCESS_TOEKEN_EXPERATION_MINS)
    access_token=create_access_token(data={"sub":db_user.username},expires_delta=expiry_period)
    return Token(access_token=access_token,token_type="bearer")

@auth_router.get("/users/me",response_model=UserResponse)
def me(user=Depends(get_user)):
    return user