from fastapi import FastAPI
from enum import Enum
app=FastAPI()
class ModelName(str,Enum):
    alexnet="alexnet"
    resnet="resnet"
    lenet="lenet"
@app.get("/items/{name}")
async def read(name:str,q:str| None=None ,short:bool=False):
    if q:
        return {"name":name,"q":q}
    return{"name":name}
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q,"description": "This is an amazing item that has a long description"})
    
        
    return item


@app.get('/model/{model_name}')
#passing the class type ONLY THE PREDEFINED
def greet(model_name:ModelName):
    if(model_name is ModelName.alexnet):
        return{"model_name":model_name,"messgae":"Deep Learning"}
    if(model_name is ModelName.lenet):
        return {"model_name": model_name, "message": "LeCNN all the images"}
    if(model_name.value=='resnet'):
        return {"model_name": model_name, "message": "Have some residuals"}
    else:
        return {"message":"No model exixst"}
    