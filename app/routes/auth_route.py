from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema.auth_schema import UserCreate,UserResponse
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth_service import register_user_service

router=APIRouter(prefix='/authorization',tags=["Authorization"])

@router.post('/register',status_code=201)
def register_user(user:UserCreate,db:Session=Depends(get_db)):
    return register_user_service(user,db)