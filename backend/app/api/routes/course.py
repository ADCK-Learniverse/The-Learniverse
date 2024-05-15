from fastapi import APIRouter, Depends
from backend.app.models import Course
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.course_services import new_course
from typing import Annotated

course_router = APIRouter(prefix="/courses")

user_dependency = Annotated[dict, Depends(get_current_user)]


@course_router.post("/new")
def create_course(user: user_dependency, course: Course):
    user_id = user.get("id")
    user_role = user.get("role")
    return new_course(user_id, user_role, course)
