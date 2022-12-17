from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from repositories.users import UserRepository
from .depends import get_user_repository, get_current_user
from models.user import User, UserIn

router = APIRouter()


@router.get("/", response_model=List[User], response_model_exclude={'hashed_password'})
async def read_user(
    users: UserRepository = Depends(get_user_repository),
    limit: int = 100,
    skip: int = 0
):
    return await users.get_all(limit=limit, skip=skip)


@router.post('/', response_model=User, response_model_exclude={'hashed_password'})
async def create_user(user: UserIn, users: UserRepository = Depends(get_user_repository)):
    return await users.create(u=user)


@router.patch("/", response_model=User, response_model_exclude={'hashed_password'})
async def update_user(id: int, user: UserIn, users: UserRepository = Depends(get_user_repository), current_user: User = Depends(get_current_user)):
    old_user = await users.get_by_id(id=id)
    if old_user is None or old_user.email != current_user.email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return await users.update(id=id, u=user)


# @router.get("/{id}", response_model=User, response_model_exclude={'hashed_password'})
# async def get_user_by_id(id: int = Path(), users: UserRepository = Depends(get_user_repository)):
#     return await users.get_by_id(id=id)


# @router.get("/{email}", response_model=User, response_model_exclude={'hashed_password'})
# async def get_by_email(email: str = Path(), users: UserRepository = Depends(get_user_repository)):
#     return await users.get_by_email(email=email)
