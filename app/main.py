
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database.connection import engine, Base
from app.routers import movement_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(movement_router.router)