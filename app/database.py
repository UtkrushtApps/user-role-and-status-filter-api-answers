import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://postgres:postgres@db:5432/postgres')

engine = create_async_engine(DATABASE_URL, echo=False, future=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

def get_async_session():
    async def _get_session():
        async with AsyncSessionLocal() as session:
            yield session
    return _get_session()
