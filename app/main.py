from fastapi import FastAPI
from app.api.routes import chat
#from .models.schemas import Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(chat.router)
