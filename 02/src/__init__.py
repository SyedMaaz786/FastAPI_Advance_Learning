from fastapi import FastAPI
from src.books.routes import book_router
from src.auth.routes import auth_router
from contextlib import asynccontextmanager
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")  #This is going to print in the console when server is starting
    await init_db() #calling the fnx
    yield
    print(f"Server has been stopped")  #This is going to print in the console when server is ending

app = FastAPI(

)

app.include_router(book_router, prefix="/books") #This is the logic to remove a common word in our url ie /books
app.include_router(auth_router, prefix="/auth") 