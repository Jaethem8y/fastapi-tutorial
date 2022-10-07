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

@app.get("/try/{path_var}")
async def path_var_path(path_var:str):
    return path_var

@app.post("/")
async def root_post(something:Something):
    return something


# Hello I am Sam