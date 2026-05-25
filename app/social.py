from fastapi import FastAPI, Body, Response, status,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,Annotated
from random import randrange
app= FastAPI()

class PostUpdate(BaseModel):
    title:str
    content:str
class Post(PostUpdate):
    published:bool=True
    rating:Optional[int]=None

my_posts=[{"title":"Dog","cotent":"Dog eating banana","rating":5,"id":1},{"title":"Cat","cotent":"Cat eating biscuits","rating":5,"id":2}]
@app.get("/post")
async def get_post():
    return {
        "data":my_posts
    }
@app.post("/post")
async def create_post(post:Post,status_code=status.HTTP_201_CREATED):
    post_data=post.dict()
    post_data["id"]=randrange(0,1000000)
    my_posts.append(post_data)
    
    return{
        "message":"post created",
        "post":post_data
    }
def see_post(id):
    for post in my_posts:
       if(post["id"]==id):
           return post

@app.get("/post/{id}")
async def get_post(id:int,response:Response):
    post=see_post(id)
    if not post:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not exist")
    return {"post":post}

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i
    return None


@app.delete("/post/{id}")
async def delete_post(id:int,status_code=status.HTTP_204_NO_CONTENT):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not exist"
        )
        
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
# @app.put("/post/{id}")
# async def update_post(id: int, post: PostUpdate):

#     postnew = see_post(id)

#     if not postnew:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=f"post with id {id} not exist"
#         )

#     postnew["title"] = post.title
#     postnew["content"] = post.content

#     return {
#         "updated_post": postnew
#     } 
# this is data coming from frontedn we convert it to the dictnary we give it id as we give after the same as that data not contanin the id  
@app.put("/post/{id}")
async def update_post(id:int,post:Post):
    index=find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not exist"
        )
    post_dict=post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data":post_dict}
