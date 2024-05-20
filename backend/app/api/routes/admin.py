from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.api.services.admin_services import view_teacher_requests, deactivate
from backend.app.api.services.login_services import get_current_user
from backend.app.api.utils.responses import Unauthorized
from backend.app.api.utils.utilities import unsubscribe, approve_request, decline_request

admin_router = APIRouter(prefix="/admin_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]


@admin_router.delete('/{course_id}/subscriber/{subscriber_id}', status_code=200)
async def remove_subscriber(user: user_dependency, course_id, subscriber_id):
    return await unsubscribe(user,course_id, subscriber_id)

@admin_router.get('/pending_requests', status_code=200)
async def view_pending_requests_from_teachers(user: user_dependency):
    return await view_teacher_requests(user)

@admin_router.patch('/registration_request', status_code=200)
async def approve_teacher_request(user: user_dependency, teacher_id):
    return await approve_request(user, teacher_id)

@admin_router.delete('/registration_request', status_code=200)
async def decline_teacher_request(user: user_dependency, teacher_id):
    return await decline_request(user, teacher_id)

@admin_router.delete('/restrict_access', status_code=200)
async def deactivate_account(user:user_dependency, person_id):
    return await deactivate(user, person_id)

# @admin_router.delete('/')
# async def delete_course(user: user_dependency, course_id: int):
#     if user is None or user.get('role') == 'student':
#         raise Unauthorized
#     return await remove_course(user.get('first_name'),user.get('last_name'), course_id)
