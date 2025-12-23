from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from src.books.routes import book_router
from src.auth.routes import auth_router
from src.reviews.routes import review_router
from contextlib import asynccontextmanager
from src.db.main import init_db
from .errors import(
    create_exception_handler,
    InvalidCredentials,
    BookNotFound,
    UserAlreadyExists,
    UserNotFound,
    InsufficientPermission,
    AccessTokenRequired,
    InvalidToken,
    RefreshTokenRequired, 
    RevokedToken,
    AccountNotVerified
)

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"Server is starting...")  #This is going to print in the console when server is starting
    await init_db() #calling the fnx
    yield
    print(f"Server has been stopped")  #This is going to print in the console when server is ending

app = FastAPI(

)

app.add_exception_handler(
        UserAlreadyExists,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_details={
                "message": "User with email already exists",
                "error_code": "user_exists",
            },
        ),
    )

app.add_exception_handler(
        UserNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_details={
                "message": "User not found",
                "error_code": "user_not_found",
            },
        ),
    )

app.add_exception_handler(
        BookNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_details={
                "message": "Book not found",
                "error_code": "book_not_found",
            },
        ),
    )

app.add_exception_handler(
        InvalidCredentials,
        create_exception_handler(
            status_code=status.HTTP_400_BAD_REQUEST,
            initial_details={
                "message": "Invalid email or password",
                "error_code": "invalid_email_or_password",
            },
        ),
    )

app.add_exception_handler(
        InvalidToken,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_details={
                "message": "Token is invalid Or expired",
                "resolution": "Please get new token",
                "error_code": "invalid_token",
            },
        ),
    )

app.add_exception_handler(
        RevokedToken,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_details={
                "message": "Token is invalid or has been revoked",
                "error_code": "token-revoked",
            },
        ),
    )

app.add_exception_handler(
        AccessTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_details={
                "message": "Please provide a valid access token",
                "resolution": "Please get an access token",
                "error_code": "access-token_required"
            },
        ),
    )

app.add_exception_handler(
        RefreshTokenRequired,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_details={
                "message": "Please provide a valid refresh token",
                "resolution": "Please get an refresh token",
                "error_code": "refresh_token_required",
            },
        ),
    )

app.add_exception_handler(
        InsufficientPermission,
        create_exception_handler(
            status_code=status.HTTP_401_UNAUTHORIZED,
            initial_details={
                "message": "You do not have enough permissions to perform this action",
                "error_code": "insufficient_permissions",
            },
        ),
    )

app.add_exception_handler(
        BookNotFound,
        create_exception_handler(
            status_code=status.HTTP_404_NOT_FOUND,
            initial_details={
                "message": "Book Not Found",
                "error_code": "book_not_found",
            },
        ),
    )

app.add_exception_handler(
        AccountNotVerified,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
            initial_details={
                "message": "Account Not verified",
                "error_code": "account_not_verified",
                "resolution":"Please check your email for verification details"
            },
        ),
    )

@app.exception_handler(500)
async def internal_server_error(request, exception):
    print(str(exception))
    return JSONResponse(
        content={
            "message": "Oops! Something Went Wrong",
            "error_code": "server_error"
        },
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
    )


app.include_router(book_router, prefix="/books") #This is the logic to remove a common word in our url ie /books
app.include_router(auth_router, prefix="/auth") 
app.include_router(review_router, prefix="/reviews")