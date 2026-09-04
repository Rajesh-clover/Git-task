from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    name : str
    description : str
    age : int

@app.post("/items")
async def create_item(item: Item):
    return {"name": item.name, "description": item.description, "age": item.age}


