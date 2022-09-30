from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Something(BaseModel):
    id:int
    name:str
    age:int

@app.get("/")
async def root():
    return "Hello World"

@app.get("/try")
async def root(message:str):
    return message

@app.post("/")
async def root_post(something:Something):
    return something