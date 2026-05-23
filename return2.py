
from pydantic import BaseModel
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str | None = None


class UserIn(BaseUser):
    password: str
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})

#we are using the inheritance here as the perobelm before is the returning the user 
@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user