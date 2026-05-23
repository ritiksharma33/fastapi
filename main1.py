from typing import Any
from pydantic import BaseModel
from datetime import datetime
class User(BaseModel):
    id:int
    name:str="Ritik"
    signup_ts: datetime | None=None
    friends:list[int]=[]
data={
    "id":"123",
    "name":"ritik",
    "signup_ts":"2017-06-01 12:22",
    "friends":[1,"2",b"3"]
}
#this is the issue of argument take one given two so we refrence it 
user=User(**data)
print(user)





def greet(fname:str,lname:str):
    name=fname.title()+" "+lname.title()
    return name
print(greet("ritik","shamra"))

def age(name:Any,age:Any):
    info=name.title()+" age is " + age
    return info
print(age("ritik","22"))

def get_items(item:list[str|int]):
    for i in item:
        print(i.title())

get_items(["grape","apple","good"])
vari={
    "name":21

}
print(vari.items())
print(vari.keys)

def employees(person:dict[str,int]):
    for i in person:
        print(i.title())
employees({"ritik":33,"preet":32})