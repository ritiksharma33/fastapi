from fastapi import FastAPI, Body, Response, status,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,Annotated
from random import randrange
import psycopg2
import time
#this will give column name as well as value 
from psycopg2.extras import RealDictCursor 
app= FastAPI()


#this is the connection string to the database 
while True:
    try:
        conn=psycopg2.connect(host="localhost",database='fastapi',user="postgres",password="1234",cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print ("Data base connection successful")
        break
    except Exception as error:
        print("connection to database failed")
        print("error",error)
        time.sleep(2)



class PostUpdate(BaseModel):
    title:str
    content:str
class Post(PostUpdate):
    published:bool=True
    

my_posts=[{"title":"Dog","cotent":"Dog eating banana","rating":5,"id":1},{"title":"Cat","cotent":"Cat eating biscuits","rating":5,"id":2}]

@app.get("/post")

async def get_post():
    cursor.execute("""SELECT * FROM posts """)
    posts=cursor.fetchall()
    print(posts)
    return {"post":posts}


@app.post("/post")
async def create_post(post:Post,status_code=status.HTTP_201_CREATED):
    #if we directly try to add lead to the sql injection santitisation by postrgeess
    cursor.execute("""INSERT INTO posts(title,content,published) VALUES (%s,%s,%s) RETURNING *""",(post.title,post.content,post.published))
    new_post=cursor.fetchone()
    conn.commit()
    return{
        "message":"post created",
        "post":new_post
    }
def see_post(id):
    for post in my_posts:
       if(post["id"]==id):
           return post
#we cannot make it string as user can type out sjhfjs but sql need string before i used str(id) if type 33 bug happen as str read char by cahr and it think i am passing the mutiple values 
#so better make it touple 
@app.get("/post/{id}")
async def get_post(id:int,response:Response):
    cursor.execute("""SELECT * FROM posts WHERE id= %s """,(id,))
    post=cursor.fetchone()
    
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
    cursor.execute("""DELETE FROM posts WHERE id=%s returning * """,(id,))
    deleted_post=cursor.fetchone()
    conn.commit()
    

    
    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not exist"
        )
        
    
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
    cursor.execute(""" UPDATE posts SET title=%s,content=%s, published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,(id,)))
    updated_post=cursor.fetchone()
    conn.commit()
    if updated_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} not exist"
        )
    
    return {"data":updated_post}
