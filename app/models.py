from .database import Base
from sqlalchemy import Column,Integer,String,Boolean

#now we will learn how to create a table in sql alchemy

class Posti(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String,nullable=False)
    published=Column(Boolean,default=True)
    
 