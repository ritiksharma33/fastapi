from fastapi import FastAPI
from pydantic import BaseModel,Field
from typing import Annotated
app=FastAPI()
class userIn(BaseModel):
    name:str =Field(min_length=2, max_length=50)
    email:str
    passward:str
class userOut(BaseModel):
    name:str
    email:str

@app.post('/signup',response_model=userOut)
async def login(user:userIn):
    return user

