from fastapi import FastAPI
from routers import router
from contextlib import asynccontextmanager
from repositories import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(title="Pracrice01", lifespan=lifespan)
app.include_router(router)