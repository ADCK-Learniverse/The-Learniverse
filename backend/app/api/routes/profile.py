from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File

from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.profile_services import update_phone, update_firstname, update_lastname, view_profile, \
    update_password, newsletter, get_pic_for_frontend
from backend.app.api.services.uploadpic_services import update_user_picture

profile_router = APIRouter(prefix="/student_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]


@profile_router.get("/profile", status_code=200)
def user_profile(user: user_dependency):

    """This method returns information about the user."""

    user_id = user.get("id")
    return view_profile(user_id)


@profile_router.get("/picture", status_code=200)
def user_profile_picture(user: user_dependency):

    """This method returns the profile picture of the user."""

    user_id = user.get("id")
    return get_pic_for_frontend(user_id)

@profile_router.put("/number", status_code=201)
def update_number(user: user_dependency, new_num: str):
    user_id = user.get("id")
    return update_phone(user_id, new_num)


@profile_router.put("/firstname", status_code=201)
def update_first_name(user: user_dependency, firstname: str):

    """This method updates the first name of the user with the inserted value he provides."""

    user_id = user.get("id")
    return update_firstname(user_id, firstname)


@profile_router.put("/lastname", status_code=201)
def update_last_name(user: user_dependency, lastname: str):

    """This method updates the last name of the user with the inserted value he provides."""

    user_id = user.get("id")
    return update_lastname(user_id, lastname)


@profile_router.put("/profile_pic", status_code=201)
def update_pic(user: user_dependency, picture: UploadFile = File(...)):

    """This method updates the profile picture of the user with the uploaded picture he provides."""

    user_id = user.get("id")
    return update_user_picture(user_id, picture)


@profile_router.put("/password", status_code=201)
def update_user_password(user: user_dependency, password: str):

    """This method updates the password of the user with the inserted value he provides."""

    return update_password(user, password)


@profile_router.post('/newsletter', status_code=200)
def subscribe_for_newsletter(email: str):

    """This method takes the inserted email and sends it to the newsletter table inside the database,
    for which he will receive emails."""

    return newsletter(email)

def profile_related_endpoints(router: APIRouter):
    router.get("/profile", status_code=200)(user_profile)
    router.get("/picture", status_code=200)(user_profile_picture)
    router.put('number', status_code=201)(update_number)
    router.put("/firstname", status_code=201)(update_first_name)
    router.put("/lastname", status_code=201)(update_last_name)
    router.put("/password", status_code=201)(update_user_password)
    router.post('/newsletter', status_code=200)(subscribe_for_newsletter)

