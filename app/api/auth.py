from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse
from app.models.users import User
from app.db.database import get_db
from app.core.security import verify_password
from app.core.jwt import create_access_token

from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login", response_model=TokenResponse)
async def login(login_data:LoginRequest,db:Session = Depends(get_db)):
    user = (db.query(User).filter(User.email == login_data.email).first())
    if user is None :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect UserName or Password"
        )
    if not verify_password(login_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect UserName or Password"
        )
    
    token = create_access_token(
        user.id,
        user.role
    )
    
    return TokenResponse(
        access_token=token,
        token_type="bearer"
    )