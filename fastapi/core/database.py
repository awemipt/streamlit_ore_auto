from os import environ
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import base_config
from models import Base

engine = create_async_engine(base_config.POSTGRES_URL, echo=True)
sync_engine = create_engine(base_config.POSTGRES_URL.replace("asyncpg", "psycopg2"))
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
try:
    if environ["DROP_TABLE_FLAG"] == "True":
        Base.metadata.drop_all(sync_engine)
except Exception as e:
    print(f"Check env or db: {e}")
Base.metadata.create_all(sync_engine)


async def get_db():
    return async_session()

