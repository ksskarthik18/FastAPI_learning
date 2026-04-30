from fastapi import APIRouter,Depends,status,HTTPException,Response
from .. import schemas,models,database
from typing import List
from sqlalchemy.orm import Session

from ..repository import blog


router = APIRouter(
    prefix ='/blog',
    tags=['Blogs']
)

get_db = database.get_db

@router.get('/',response_model = List[schemas.ShowBlog])
def all(db : Session = Depends(get_db)):
    # blogs = db.query(models.Blog).all()
    # return blogs
    return blog.get_all(db)


@router.post('/',status_code =status.HTTP_201_CREATED)
def create(request : schemas.Blog,db : Session = Depends(get_db) ):
    # new_blog = models.Blog(title = request.title,body = request.body,user_id = request.user_id)
    # db.add(new_blog)
    # db.commit()
    # db.refresh(new_blog)
    # return new_blog

    return blog.create(request,db)


@router.delete('/{id}',status_code = status.HTTP_204_NO_CONTENT)
def destory(id : int,db : Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")
    
    # blog.delete(synchronize_session=False)
    # db.commit()
    # return 'done'
    return blog.destroy(id,db)


@router.put('/{id}',status_code = status.HTTP_202_ACCEPTED)
def update(id : int, request : schemas.Blog ,db : Session = Depends(get_db)):
    # blog=db.query(models.Blog).filter(models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog with id {id} not found")
    # blog.update(request.dict())

    # db.commit()
    # return 'updated sucessfully'
    return blog.update(id,request,db)



@router.get('/{id}',status_code=200,response_model = schemas.ShowBlog)
def show(id : int,db : Session = Depends(get_db)):
    # blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # if not blog:
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {'detail' : f"Blog with the {id} is not available"}
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"Blog with the {id} is not available" ) 
    # return blog

    return blog.show(id,db)
