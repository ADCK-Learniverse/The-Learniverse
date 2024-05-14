from typing import Annotated
from starlette import status
from data.database import read_query
import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from services.admin_services import get_user_by_id, logged_in_users
from dotenv import load_dotenv
import os

load_dotenv()

ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = 15

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        secret_key = os.getenv('SECRET_KEY')
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("user_id")
        user_role: str = payload.get("role")
        if username is None or user_id is None:
            raise credentials_exception
        return {"username": username, "id": user_id, "role": user_role}
    except JWTError:
        raise credentials_exception


def generate_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})
    secret_key = os.getenv('SECRET_KEY')
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str):
    username_sql = 'SELECT * FROM users WHERE username = %s'
    password_sql = 'SELECT password FROM users WHERE username = %s'
    username_data = read_query(username_sql, (username,))
    password_data = read_query(password_sql, (username,))
    if not username_data:
        raise HTTPException(status_code=404, detail='Incorrect username or password!')
    return bcrypt.checkpw(password.encode('utf-8'), password_data[0][0].encode('utf-8'))


def login(username: str, password: str):
    if authenticate_user(username, password):
        id_query = 'SELECT user_id FROM users WHERE username = %s'
        get_id = read_query(id_query, (username,))
        user_id = get_id[0][0]
        role_query = 'SELECT role FROM users WHERE username = %s'
        get_role = read_query(role_query, (username,))
        user_token = generate_token({'sub': username, 'user_id': user_id,
                                    'role': get_role[0][0]})
        logged_in_users.update({f'{user_id}': {'Username': username}})
        return {
                    "access_token": user_token,
                    "token_type": "bearer"
                }
    else:
        raise HTTPException(status_code=404, detail='Incorrect username or password!')


def logout(user_id: int):
    user = get_user_by_id(user_id)
    if user and str(user_id) in logged_in_users:
        logged_in_users.popitem()
        return {'message': 'You have successfully logged out!'}
    else:
        raise HTTPException(status_code=404, detail='No such user is logged in!')
