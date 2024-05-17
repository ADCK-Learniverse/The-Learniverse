from fastapi import APIRouter, Depends

from backend.app.api.utils.responses import Unauthorized
from backend.app.models import Course
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.course_services import new_course, switch_status, remove_course
from typing import Annotated

course_router = APIRouter(prefix="/courses")

user_dependency = Annotated[dict, Depends(get_current_user)]


@course_router.post("/new", status_code=201)
def create_course(user: user_dependency, course: Course):
    if user is None or user.get('role') == 'student':
        raise Unauthorized

    user_id = user.get("id")
    user_role = user.get("role")
    return new_course(user_id, user_role, course)


@course_router.put("/status", status_code=200)
def switch_course_status(user: user_dependency, course_id: int):
    if user is None or user.get('role') == 'student':
        raise Unauthorized

    user_role = user.get("role")
    user_id = user.get("id")
    return switch_status(course_id, user_role, user_id)

@course_router.delete('/')
async def delete_course(user: user_dependency, course_id: int):
    if user is None or user.get('role') == 'student':
        raise Unauthorized
    return await remove_course(user.get('first_name'),user.get('last_name'), course_id)