from fastapi import FastAPI
from app.database import engine
from app.models.base import Base
from app.routes.auth_route import router as auth_router

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)