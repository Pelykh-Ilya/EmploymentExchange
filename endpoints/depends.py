from fastapi import Depends, HTTPException, status
from repositories.users import UserRepository
from repositories.jobs import JobsRepository
from db.base import database
from models.user import User
from models.token import Token
from core.security import JWTBearer, decode_acess_token

def get_user_repository() -> UserRepository:
    return UserRepository(database)

def get_job_repository() -> JobsRepository:
    return JobsRepository(database)

async def get_current_user(
    users: UserRepository = Depends(get_user_repository),
    token: Token = Depends(JWTBearer())
) -> User:
    cred_exception = HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    payload = decode_acess_token(token=token)
    if payload is None:
        raise cred_exception
    
    email: str = payload.get('sub')
    if email is None:
        raise cred_exception

    user = await users.get_by_email(email=email)
    if user is None:
        raise cred_exception
    return user