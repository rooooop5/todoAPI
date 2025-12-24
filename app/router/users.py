from fastapi import APIRouter,Depends,Query,HTTPException,Response
from sqlmodel import Session,select
from app.models.user_models import User,UserCreate,UserResponse,UserPatch
from app.models.task_models import TaskResponse
from app.core.database import get_session



users_router=APIRouter(prefix='/users',tags=['users'])

@users_router.get("/",response_model=list[UserResponse])
def get_users(session:Session=Depends(get_session)):
    db_users=session.exec(select(User)).all()
    return db_users

@users_router.get("/{user_id}",response_model=UserResponse)
def get_user(user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    return db_user


@users_router.get("/{user_id}/tasks",response_model=list[TaskResponse])
def get_user_tasks(user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    user_tasks=db_user.tasks
    return user_tasks

@users_router.post("/",response_model=UserResponse)
def create_user(user:UserCreate,session:Session=Depends(get_session)):
    db_user=User(**user.model_dump())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@users_router.put("/{user_id}",response_model=UserResponse)
def put_user(user:UserCreate,user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    user_data=user.model_dump(exclude={"id"})
    db_user.sqlmodel_update(user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


@users_router.patch("/{user_id}",response_model=UserResponse)
def patch_user(user:UserPatch,user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    user_data=user.model_dump(exclude_unset=True)
    db_user.sqlmodel_update(user_data)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user

@users_router.delete("/{user_id}")
def delete_user(user_id:int,session:Session=Depends(get_session)):
    db_user=session.get(User,user_id)
    if db_user.tasks:
        raise HTTPException(status_code=409,detail="409 ERROR : User has existing tasks,cannot delete.")
    session.delete(db_user)
    session.commit()
    return Response(status_code=204)