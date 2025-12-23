from fastapi import APIRouter, Depends, Query,HTTPException,Response
from sqlmodel import Session, select
from app.core.database import get_session
from app.models.task_models import Task
from app.models.task_models import Status,Priority
from datetime import date


tasks_router = APIRouter(prefix='/tasks', tags=['tasks'])

#------GET endpoint------
@tasks_router.get('/')
def get_tasks(status:Status=Query(default=None), priority:Priority=Query(default=None), session: Session = Depends(get_session)):
    query=select(Task)
    if status is not None:
        query=query.where(Task.status==status)
    if status is not None:
        query=query.where(Task.priority==priority)
    db_tasks=session.exec(query).all()
    return db_tasks


#------GET by due date------
@tasks_router.get('/due')
def get_by_due_date(due_date:date|None=Query(default=None),session:Session=Depends(get_session)):
    if not due_date:
        db_tasks=session.exec(select(Task)).all()
        return db_tasks
    db_tasks=session.exec(select(Task).where(Task.due_date==due_date)).all()
    return db_tasks


#------GET by due date------
@tasks_router.get('/overdue')
def get_overdue_tasks(session:Session=Depends(get_session)):
    db_tasks=session.exec(select(Task).where(Task.due_date.is_not(None))).all()
    overdue_tasks=[]
    for task in db_tasks:
        if task.due_date<date.today():
            if task.status==Status.PENDING:
                overdue_tasks.append(task)
    if not overdue_tasks:
        return {"message":"There are no overdue tasks."}
    return overdue_tasks


#------GET by ID endpoint------
@tasks_router.get('/{task_id}')
def get_tasks_by_id(task_id:int, session: Session = Depends(get_session)):
    task = session.get(Task,task_id)
    if not task:
        raise HTTPException(status_code=404,detail="404 ERROR : Task not found.")
    return task





#------POST endpoint------
@tasks_router.post('/')
def create_tasks(task: Task, session: Session = Depends(get_session)):
    task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        status=task.status,
        priority=task.priority,
    )
    session.add(task)
    session.commit()
    session.refresh(task)
    return task


#------PUT endpoint------
@tasks_router.put('/{task_id}')
def put_tasks(task_id:int,task:Task,session:Session=Depends(get_session)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(status_code=404,detail="404 ERROR : Task not found.")
    task_data=task.model_dump(exclude={'id'})
    db_task.sqlmodel_update(task_data)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


#------PUT endpoint------
@tasks_router.patch('/{task_id}')
def patch_tasks(task_id:int,task:Task,session:Session=Depends(get_session)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(status_code=404,detail="404 ERROR : Task not found.")
    task_data=task.model_dump(exclude_unset=True)
    db_task.sqlmodel_update(task_data)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


#------DELETE endpoint------
@tasks_router.delete('/{task_id}')
def delete_task(task_id:int,session:Session=Depends(get_session)):
    db_task=session.get(Task,task_id)
    if not db_task:
        raise HTTPException(status_code=404,detail="404 ERROR : Task not found.")
    session.delete(db_task)
    session.commit()
    return Response(status_code=204)