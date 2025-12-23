from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.router import tasks
from app.core.database import _init_table


@asynccontextmanager
async def lifespan(app: FastAPI):
    _init_table()
    yield
    print('Shutting down the API.')


app = FastAPI(lifespan=lifespan)


@app.get('/')
def home():
    return {'Message': 'This is a Todo Application.'}


app.include_router(tasks.tasks_router)
