import jwt
from datetime import datetime , timedelta
from app.core.config import settings
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.users import User


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def create_access_token(user_id : str,role: str)->str:
    expire = datetime.utcnow()+ timedelta(minutes=settings.access_token_expire_minutes)

    payload = {
        "sub" : user_id,
        "role" : role,
        "exp" : expire,
    }

    token = jwt.encode(payload,settings.secret_key,algorithm=settings.algorithm)
    return token

def decode_access_token(token:str)->dict:
    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )
        return payload
    except InvalidTokenError:
        return None
    
async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
        payload = decode_access_token(token)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
            )
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication credentials"
         )
        user = db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        return user