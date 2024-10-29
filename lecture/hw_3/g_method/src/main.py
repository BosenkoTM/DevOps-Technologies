from fastapi import FastAPI
from .database import engine
from . import models

app = FastAPI(title="FastAPI Project", description="Simple FastAPI project with PostgreSQL")

# Создаем таблицы при запуске
models.Base.metadata.create_all(bind=engine)

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Project"}