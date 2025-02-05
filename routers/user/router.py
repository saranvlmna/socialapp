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

# @user_router.post("/login")
# def login(db:Session=Depends(get_db)):
#     return crud.list_all_users(db)

# @user_router.patch("/{user_id}")
# def update_user(user_id: int, db: Session = Depends(get_db)):
#     return crud.get_user(db, user_id)

# @user_router.delete("/{username}")
# def delete_user(username: str, db: Session = Depends(get_db)):
#     return crud.get_user_by_username(db, username)