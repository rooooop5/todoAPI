from contextlib import asynccontextmanager
from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
from app.router import tasks
from app.core.database import _init_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    _init_table()
    yield
    print('Shutting down the API.')


app = FastAPI(lifespan=lifespan)


@app.exception_handler(HTTPException)
def handler(request:Request,exception:HTTPException):
    return JSONResponse(
        status_code=exception.status_code,
        content={
            "error":{
                "status_code":exception.status_code,
                "message":exception.detail,
                "path":request.url.path
                }
            }
    )




@app.get('/')
def home():
    return {'Message': 'This is a Todo Application.'}


app.include_router(tasks.tasks_router)
