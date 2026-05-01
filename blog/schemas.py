from pydantic import BaseModel, ConfigDict
from typing import List,Optional

class BlogBase(BaseModel):
    title : str
    body : str
    user_id : int
class Blog(BlogBase):
    model_config = ConfigDict(from_attributes=True)


class ShowUser(BaseModel):
    id : int
    name : str
    email : str
    blogs : List[Blog] =[]
    model_config = ConfigDict(from_attributes=True)


class ShowBlog(BaseModel):
    title : str
    body : str
    creator : ShowUser
    model_config = ConfigDict(from_attributes=True)
    
class User(BaseModel):
    name: str
    email: str
    password: str


class Login(BaseModel):
    username: str 
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    email : Optional[str] = None





