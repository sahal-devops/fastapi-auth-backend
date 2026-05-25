from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status
)

from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from app.database import SessionLocal
from app.models.user import User
from app.schemas.user import UserCreate

from app.auth.jwt_handler import (
    create_access_token,
    verify_token
)

print("AUTH ROUTES LOADED")

router = APIRouter()

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# Register Route
@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    # Check existing username
    existing_username = db.query(User).filter(
        User.username == user.username
    ).first()

    if existing_username:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    # Check existing email
    existing_email = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_email:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

    # Hash password
    hashed_password = pwd_context.hash(
        user.password
    )

    # Create new user
    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password,
        role="user"
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "User registered successfully",
        "username": new_user.username,
        "email": new_user.email,
        "role": new_user.role
    }


# Login Route
@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # Find user by email
    db_user = db.query(User).filter(
        User.email == form_data.username
    ).first()

    # Invalid email
    if not db_user:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email"
        )

    # Invalid password
    if not pwd_context.verify(
        form_data.password,
        db_user.password
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    # Create JWT token
    token = create_access_token(
        {
            "sub": db_user.email,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "role": db_user.role
    }


# Profile Route
@router.get("/profile")
def profile(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    # Invalid token
    if payload is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    return {
        "message": "Protected route accessed",
        "user": payload
    }


# Admin Route
@router.get("/admin")
def admin_route(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    # Invalid token
    if payload is None:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

    # Role check
    if payload.get("role") != "admin":

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )

    return {
        "message": "Welcome Admin",
        "user": payload
    }