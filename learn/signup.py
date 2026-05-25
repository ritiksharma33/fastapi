from fastapi import FastAPI,Path,HTTPException
from pydantic import BaseModel,Field
from typing import Annotated
from enum import Enum



app=FastAPI()
class courseName(str,Enum):
    python="Python"
    java="Java"
    c="C"

class StudentPublic(BaseModel):
    id:int
    name:str
    course:courseName
    fees:int
    address: str | None = None
    
class StudentPrivate(StudentPublic):
    phone:int
    password:str

class Login(BaseModel):
    
    gmail:str
    password:str
class role(str,Enum):
    student="student"
    admin="admin"

class Signup(Login):
    role:role
    name:str

class StudentUpdate(BaseModel):
    fees: int | None = None
    address: str | None = None




students = {
    1: {
        "id": 1,
        "name": "Ritik",
        "course": "Python",
        "fees": 50000,
        "address": "Delhi",
        "phone": 9999999999,
        "password": "ritik123"
    },
    2: {
        "id": 2,
        "name": "Aman",
        "course": "Java",
        "fees": 45000,
        "phone": 8888888888,
        "password": "aman123"
    }
}

users = {}

@app.post("/signup")
async def create_user(user:Signup):
    for i in users.values():
        if i["gmail"]==user.gmail:
            raise HTTPException(
                status_code=400,
                detail="User already exixts"
            )
    new_id=len(users)+1
    users[new_id]={
            "id":new_id,
            "name":user.name,
            "gmail":user.gmail,
            "password":user.password,
            "role":user.role
        }
    return {
            "message":"Signup successfull",
            "user":users[new_id]
        }
#Login 
@app.post("/login")
async def login_user(user:Login):
    for i in users.values():
        if i['gmail']==user.gmail and i['password']==user.password:

          return {
        "message":"Login Successfull",
        "role":i['role']
               }
        raise HTTPException(
            status_code=400,
            detail="Signup no user found"
        )


@app.get("/students/{id}",response_model=StudentPublic)
async def get_student(
    id: Annotated[int, Path(gt=0, lt=100)]
):
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[id]

@app.get("/admin/student/{id}",response_model=StudentPrivate)
async def get_student_private(
    id: Annotated[int, Path(gt=0, lt=100)]
):   
    if id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return students[id]


@app.post("/admin/create-student",response_model=StudentPrivate)
async def create_student(user:StudentPrivate):
    if user.id in students:
        raise HTTPException(
            status_code=400,
            detail="Student ID already exists"
        )
    students[user.id]=user.dict()

    

    return students[user.id]

@app.delete("/admin/delete-student/{id}")
async def delete_student(id:int):
    if id not in students:
        raise HTTPException(
            status_code=400,
            detail="not does not exist "
        )
    del students[id]
    return {
        "message":"student deleted successfully"
    }
@app.put("/admin/update/{id}")
async def update_student(id:int ,user:StudentUpdate):
    if id not in students:
        raise HTTPException(
            status_code=400,
            detail="Student does not exixt"
        )
    #this is the case user provided the all field but what if the are some field to update 

    #students[user.id]=user.dict()
    if user.fees is not None:
        students[id]["fees"]=user.fees
    if user.address is not None:
        students[id]["address"]=user.address
    return {
        "message":"Student updated successfully",
        "updated_student":students[id]
        }


