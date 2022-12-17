from typing import List

from fastapi import APIRouter, Depends, HTTPException, status

from models.jobs import Job, JobIn
from models.user import User
from repositories.jobs import JobsRepository
from .depends import get_job_repository, get_current_user

router = APIRouter()


@router.get('/', response_model=List[Job])
async def read_jobs(
    jobs: JobsRepository = Depends(get_job_repository),
    limit: int = 100,
    skip: int = 0
):
    return await jobs.get_all(limit=limit, skip=skip)


@router.post('/', response_model=Job)
async def create_jobs(j: JobIn,
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    return await jobs.create(user_id= current_user.id, j=j)


@router.patch('/', response_model=Job)
async def update_jobs(
    id: int,
    j: JobIn,
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)
):
    job = await jobs.get_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return await jobs.update(id=id, user_id=current_user.id, j=j)


@router.delete('/')
async def delete_jobs(
    id: int,
    jobs: JobsRepository = Depends(get_job_repository),
    current_user: User = Depends(get_current_user)):
    job = await jobs.get_by_id(id=id)
    if job is None or job.user_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    await jobs.delete(id=id)
    return job