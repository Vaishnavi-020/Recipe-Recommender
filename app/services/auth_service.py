from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.users import User
from app.schema.auth_schema import UserCreate
from app.core.security import hash_password,verify_password
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

def register_user_service(user:UserCreate,db:Session):
    existing_user=db.query(User).filter(User.email==user.email).first()
    if existing_user:
        raise HTTPException(status_code=406,detail='User with this email already exists')
    else:
        new_user=User(name=user.name,
                      email=user.email,
                      password_hash=hash_password(user.password))

        db.add(new_user)
        db.commit()
    return {
        'user':user.name,
        'email':user.email
    }