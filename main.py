from fastapi import FastAPI
from database import engine
from database import Base
from routers import post_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post_router.router)