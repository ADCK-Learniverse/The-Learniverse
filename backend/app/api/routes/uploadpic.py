from fastapi import APIRouter, UploadFile, File, Depends
from typing import Annotated
from backend.app.api.services.uploadpic_services import update_user_picture, update_course_picture
from backend.app.api.services.login_services import get_current_user

picture_router = APIRouter(prefix="/picture")

user_dependency = Annotated[dict, Depends(get_current_user)]


@picture_router.put("/profile/{user_id}", status_code=201)
def upload_profile_pic(user: user_dependency, picture: UploadFile = File(...)):
    user_id = user.get("id")
    return update_user_picture(user_id, picture)


@picture_router.put("/course/{course_id}", status_code=201)
def upload_course_pic(user: user_dependency, course_id: int, picture: UploadFile = File(...)):
    user_role = user.get("role")
    user_id = user.get("id")
    return update_course_picture(user_id, user_role, course_id, picture)
