from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from model.connection import get_db 
from pydantic import BaseModel
from . import post_create

post_router = APIRouter(
    prefix='/post',
    tags=['post']
)

class Post(BaseModel):
    title: str
    discription: str
    url:str

@post_router.post("/")
def create_post(post:Post, db: Session = Depends(get_db)):
    return post_create.create(db,post)