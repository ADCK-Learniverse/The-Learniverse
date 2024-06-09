from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from backend.app.api.services.login_services import logout, login

login_router = APIRouter(prefix='/login')
logout_router = APIRouter(prefix='/logout')

all_users = {}


@login_router.post('/token', status_code=201)
def user_login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """
    This method takes the user's email and password, logs them in, and returns a token.
    """
    return login(form_data.username, form_data.password)


@logout_router.post('', status_code=204)
def user_logout(user_id: int):
    """
    This method takes in the logged user's ID and logs them out.
    """
    return logout(user_id)



