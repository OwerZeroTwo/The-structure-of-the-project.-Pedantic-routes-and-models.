from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}

from .routers import router

app.include_router(router)