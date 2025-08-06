from fastapi import FastAPI
from app.handlers.users import router as user_router
from app.db.database import async_engine, Base #noqa
from app.db.init_db import init_models
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_models()
    print("Database initialized")
    yield
    await async_engine.dispose()

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)


