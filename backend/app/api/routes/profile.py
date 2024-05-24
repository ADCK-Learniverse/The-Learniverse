from typing import Annotated

from fastapi import APIRouter, Depends, UploadFile, File

from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.profile_services import update_phone, update_firstname, update_lastname, view_profile, \
    update_password
from backend.app.api.services.uploadpic_services import update_user_picture

profile_router = APIRouter(prefix="/student_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]


@profile_router.get("/profile", status_code=200)
def user_profile(user: user_dependency):
    user_id = user.get("id")
    return view_profile(user_id)

@profile_router.put("/number", status_code=201)
def update_number(user: user_dependency, new_num: str):
    user_id = user.get("id")
    return update_phone(user_id, new_num)


@profile_router.put("/firstname", status_code=201)
def update_first_name(user: user_dependency, firstname: str):
    user_id = user.get("id")
    return update_firstname(user_id, firstname)


@profile_router.put("/lastname", status_code=201)
def update_last_name(user: user_dependency, lastname: str):
    user_id = user.get("id")
    return update_lastname(user_id, lastname)


@profile_router.put("/profile_pic", status_code=201)
def update_pic(user: user_dependency, picture: UploadFile = File(...)):
    user_id = user.get("id")
    return update_user_picture(user_id, picture)

@profile_router.put("/password", status_code=201)
def update_user_password(user: user_dependency, password: str):
    return  update_password(user, password)

def profile_related_endpoints(router: APIRouter):
    router.get("/profile", status_code=200)(user_profile)
    router.put("/firstname", status_code=201)(update_first_name)
    router.put("/lastname", status_code=201)(update_last_name)
    router.put("/profile_pic", status_code=201)(update_pic)
    router.put("/password", status_code=201)(update_user_password)
