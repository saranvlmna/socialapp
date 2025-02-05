from sqlalchemy.orm import Session
from model.model_user import User

def signup(db: Session, user):
    print("userrrr",user)
    # password=str(hash(password))
    # db_user = User(username=username, email=email, password=password)
    # db.add(db_user)
    # db.commit()
    # db.refresh(db_user)
    # return db_user
