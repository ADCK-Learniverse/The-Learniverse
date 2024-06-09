from typing import Annotated
from starlette import status
from backend.app import data
import bcrypt
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from backend.app.api.services.admin_services import get_user_by_id
from backend.app.api.utils.responses import NotFound, AccountNotApproved
from dotenv import load_dotenv
import os

from backend.app.data.database import read_query, update_query

load_dotenv()

ALGORITHM = 'HS256'
TOKEN_EXPIRE_MINUTES = 60

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")

logged_in_users = {}


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
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
        user_first_name = payload.get("first_name")
        user_last_name = payload.get("last_name")
        user_phone_number = payload.get("phone_number")
        last_activity_str = payload.get("last_activity")

        if username is None or user_id is None:
            raise credentials_exception

        last_activity = datetime.strptime(last_activity_str, "%Y-%m-%d %H:%M:%S.%f")

        now = datetime.utcnow()
        if now - last_activity > timedelta(minutes=15):
            raise credentials_exception

        new_token = generate_token({
            'sub': username,
            'user_id': user_id,
            'first_name': user_first_name,
            'last_name': user_last_name,
            'role': user_role,
            'phone_number': user_phone_number,
            'last_activity': now.strftime("%Y-%m-%d %H:%M:%S.%f")
        })

        user_data = {
            "email": username,
            "id": user_id,
            "role": user_role,
            'first_name': user_first_name,
            'last_name': user_last_name,
            'phone_number': user_phone_number,
            "new_token": new_token
        }

        return user_data

    except JWTError:
        raise credentials_exception


def generate_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire, 'last_activity': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")})
    secret_key = os.getenv('SECRET_KEY')
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=ALGORITHM)
    return encoded_jwt


def authenticate_user(username: str, password: str):
    username_sql = 'SELECT email FROM users WHERE email = %s'
    password_sql = 'SELECT password FROM users WHERE email = %s'
    username_data = data.database.read_query(username_sql, (username,))
    password_data = data.database.read_query(password_sql, (username,))
    if not username_data:
        raise HTTPException(status_code=404, detail='Incorrect email or password!')
    return bcrypt.checkpw(password.encode('utf-8'), password_data[0][0].encode('utf-8'))


def login(username: str, password: str):
    check_if_account_status_is_approved(username) # Stop him at the entrance if he is not approved.


    if authenticate_user(username, password):
        user_information = data.database.read_query('SELECT * FROM users WHERE email = %s', (username,))
        user_token = generate_token({'sub': username, 'user_id': user_information[0][0],
                                     'first_name': user_information[0][3], 'last_name': user_information[0][4],
                                     'role': user_information[0][5], 'phone_number': user_information[0][6]})

        logged_in_users.update({f'{user_information[0][0]}': {'Email': username}})
        return {
            "access_token": user_token,
            "token_type": "bearer"
        }
    else:
        raise NotFound


def logout(user_id: int):
    user = get_user_by_id(user_id)
    if user and str(user_id) in logged_in_users:
        logged_in_users.popitem()
        return {'message': 'You have successfully logged out!'}
    else:
        raise NotFound


def check_if_account_status_is_approved(username):
    info = read_query('SELECT status FROM users WHERE email = %s', (username,))
    if info[0][0] != 'approved':
        raise AccountNotApproved

async def password(email):
    info =  read_query('SELECT * FROM users WHERE email = %s', (email,))
    if info:
        update_query('UPDATE users SET password = %s WHERE email = %s', (new_password, email))