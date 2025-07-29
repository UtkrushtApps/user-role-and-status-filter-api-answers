from fastapi import FastAPI, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import select
from typing import List, Optional
import os

from .models import User
from .database import get_async_session
from .schemas import UserOut

app = FastAPI()

@app.get("/users", response_model=List[UserOut])
async def list_users(
    role: Optional[str] = Query(None, description="Role to filter by"),
    status: Optional[str] = Query(None, description="Status to filter by"),
    session: AsyncSession = Depends(get_async_session)
):
    stmt = select(User)
    if role:
        stmt = stmt.where(User.role == role)
    if status:
        stmt = stmt.where(User.status == status)
    result = await session.execute(stmt)
    users = result.scalars().all()
    return users
