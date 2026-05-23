from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app=FastAPI()
class Image(BaseModel):
    url:HttpUrl
    name:str
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str]=set()
    images:list[Image] | None=None

@app.put("/items/{items_id}")
async def update_item( item: Item ,items_id:int):
    results={"items_id":items_id,"item":item}
    return results
