from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from model.connection import get_db 
from pydantic import BaseModel
from . import user_signup

user_router = APIRouter(
    prefix='/user',
    tags=['user']
)

class User(BaseModel):
    name: str
    email: str
    age: int
    password:str

@user_router.post("/")
def signup(user:User, db: Session = Depends(get_db)):
    return user_signup.signup(db,user)