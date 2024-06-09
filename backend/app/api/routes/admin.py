from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.api.routes.course import course_related_endpoints
from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.routes.teacher import teacher_related_endpoints
from backend.app.api.services.admin_services import view_teacher_requests, deactivate
from backend.app.api.services.login_services import get_current_user

from backend.app.api.utils.utilities import  approve_teacher, decline_teacher


user_dependency = Annotated[dict, Depends(get_current_user)]
admin_router = APIRouter(prefix="/admin_panel")

profile_related_endpoints(admin_router)
course_related_endpoints(admin_router)
teacher_related_endpoints(admin_router)


@admin_router.get('/teacher/pending_requests', status_code=200)
async def view_pending_requests_from_teachers(user: user_dependency):
    """This method views the pending registration requests from teachers."""
    return await view_teacher_requests(user)

@admin_router.patch('/teacher/registration_request', status_code=200)
async def approve_teacher_request(user: user_dependency, teacher_id: int):
    """This method approves one by one each registration request from teachers."""
    return await approve_teacher(user, teacher_id)

@admin_router.delete('/teacher/registration_request', status_code=200)
async def decline_teacher_request(user: user_dependency, teacher_id: int):
    """This method declines one by one each registration request from teachers."""
    return await decline_teacher(user, teacher_id)

@admin_router.delete('/restrict_access', status_code=200)
async def deactivate_account(user:user_dependency, person_email: str):
    """This method deactivates the account of the desired person and restricts his access to everything."""
    return await deactivate(user, person_email)


def admin_related_endpoints(router: APIRouter):
    router.get('/pending_requests', status_code=200)(view_pending_requests_from_teachers)
    router.patch('/registration_request', status_code=200)(approve_teacher_request)
    router.delete('/registration_request', status_code=200)(decline_teacher_request)
    router.delete('/restrict_access', status_code=200)(deactivate_account)
