from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import AsyncGenerator
from sqlalchemy.orm import sessionmaker
from src.config import Config

async_engine = AsyncEngine(   #Created a engine
    create_engine(         #Create a connection engine that lets your app talk to the database(pg) asynchronously
    url = Config.DATABASE_URL,
    echo=True
))

async def init_db():
    async with async_engine.begin() as conn:  #This function opens a database connection asynchronously, runs a simple SQL query, and prints the result.
        from src.books.models import BookModel

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    
    Session = sessionmaker(
        bind = async_engine,
        class_= AsyncSession,
        expire_on_commit = False
    )

    async with Session() as session:
        yield session