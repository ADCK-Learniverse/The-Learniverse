from typing import Annotated
from fastapi import APIRouter, Depends, Query, UploadFile, File
from backend.app.api.services.login_services import get_current_user
from backend.app.api.routes.course import view_all_courses, view_course
from backend.app.api.services.student_services import (view_profile, welcome_message, view_subscriptions,
                                                       update_phone, update_firstname, update_lastname)
from backend.app.api.services.uploadpic_services import update_user_picture

student_router = APIRouter(prefix="/student_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]


@student_router.get("/")
async def home(user: user_dependency):
    user_id = user.get("id")
    return welcome_message(user_id)


@student_router.get("/courses/all", status_code=200)
def student_all_courses_view(user: user_dependency, search: str = None,
                             page: int = Query(1, ge=1),
                             size: int = Query(10, ge=1, le=100)):
    return view_all_courses(search, page, size)


@student_router.get("/courses/{course_id}", status_code=200)
def student_course_view(user: user_dependency, course_id: int):
    return view_course(user, course_id)


@student_router.get("/profile", status_code=200)
def student_profile(user: user_dependency):
    user_id = user.get("id")
    return view_profile(user_id)


@student_router.get("/subscriptions", status_code=200)
def subscriptions(user: user_dependency, page: int = Query(1, ge=1),
                  size: int = Query(10, ge=1, le=100)):
    user_id = user.get("id")
    user_role = user.get("role")
    return view_subscriptions(user_id, user_role, page, size)


@student_router.put("/number", status_code=201)
def update_number(user: user_dependency, new_num: str):
    user_id = user.get("id")
    return update_phone(user_id, new_num)


@student_router.put("/firstname", status_code=201)
def update_first_name(user: user_dependency, firstname: str):
    user_id = user.get("id")
    return update_firstname(user_id, firstname)


@student_router.put("/lastname", status_code=201)
def update_last_name(user: user_dependency, lastname: str):
    user_id = user.get("id")
    return update_lastname(user_id, lastname)


@student_router.put("/profilepic", status_code=201)
def update_pic(user: user_dependency, picture: UploadFile = File(...)):
    user_id = user.get("id")
    return update_user_picture(user_id, picture)
