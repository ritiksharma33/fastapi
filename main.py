from fastapi import FastAPI

app=FastAPI()
@app.get('/')
def str():
    return{
        "message":"server is running"
    }


@app.get('/{name}')
def greeti(name:str):
    return{
        "name":name
    }
@app.get('/items/{item_id}')
def greet(item_id:int):
    
    return {"id":item_id}