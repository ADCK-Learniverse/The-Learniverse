from typing import Annotated
from fastapi import APIRouter, Depends, Query

from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.services.login_services import get_current_user
from backend.app.api.routes.course import view_all_courses, view_course
from backend.app.api.services.student_services import (welcome_message, view_subscriptions)


student_router = APIRouter(prefix="/student_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]

profile_related_endpoints(student_router)


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


@student_router.get("/subscriptions", status_code=200)
def subscriptions(user: user_dependency, page: int = Query(1, ge=1),
                  size: int = Query(10, ge=1, le=100)):
    user_id = user.get("id")
    user_role = user.get("role")
    return view_subscriptions(user_id, user_role, page, size)

