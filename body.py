from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class Item(BaseModel):
    name:str | None=None
    decription:str 
    price: float
    tax:float | None=None


@app.post("/itmes")
async def create(item:Item):
    item_dic=item.model_dump()
    if item.tax is not None:
        item_price=item.tax+item.price
        item_dic.update({"Price with tax":item_price})
    return item_dic



  
