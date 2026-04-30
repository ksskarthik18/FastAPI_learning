from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get('/blog')

def index(limit =10,published:bool=True,sort:Optional[str]=None):
    if published:
        return {f'{limit} {published} blogs from the DB'}
    else:
        return {f'{limit}    blogs from the DB'}


@app.get('/hello')
def hello():
    return {'data':{'fastapi':'bitfumes'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished files'}


@app.get('/blog/{blog_id}')

def show(blog_id : int):
    return {'blog_id': blog_id}



@app.get('/blog/{id}/comments')
def comments(id,limit=30):
    return {'data':{'1','2'},'li':{limit}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')

def create_blog(request:Blog):
    return {'data':f'blog is created title is {request.title}'}


if __name__ == '__main__' :
    uvicorn.run(app,host="127.0.0.1",port = 9000)