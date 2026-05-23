from fastapi import FastAPI, Cookie, Header

from pydantic import BaseModel 
from typing import Annotated
app=FastAPI()

class cookie(BaseModel):
    session_id:str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None
class CommonHeaders(BaseModel):
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get('/items')
async def read_items(cookies:Annotated[cookie,Cookie()],header:Annotated[CommonHeaders,Header()]):
    return cookie
 
