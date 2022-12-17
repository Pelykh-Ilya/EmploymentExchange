from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class JobIn(BaseModel):
    title: str
    description: str
    salary_from: int
    salary_to: int
    is_active: bool = True


class Job(JobIn):
    id: Optional[int] = None
    user_id: int
    created_at: datetime
    updated_at: datetime
    