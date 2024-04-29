from fastapi import FastAPI
from db import Base, engine

from routers import user_auth

app = FastAPI()
app.include_router(user_auth.router)

Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"Hello": "World"}