from typing import Annotated

from fastapi import APIRouter, Depends
from backend.app.api.services.login_services import get_current_user
from backend.app.api.utils.responses import Unauthorized
from backend.app.api.services.teacher_services import get_information, update_information, course_subscribers
from backend.app.api.utils.utilities import unsubscribe
from backend.app.models import UpdateProfile

teacher_router = APIRouter(prefix='/teacher_panel')

user_dependency = Annotated[dict, Depends(get_current_user)]
# information = user_dependency[0]
@teacher_router.get('/', status_code=200)
async def account_information(user: user_dependency):

    if user is None or user.get('role').lower() == 'teacher':
        raise Unauthorized

    return await get_information(user)


@teacher_router.patch('/personal_information', status_code=200)
async def update_personal_information(user: user_dependency, update: UpdateProfile):
    if user is None or user.get('role').lower() == 'student':
        raise Unauthorized

    return await update_information(user.get('id'), update)


@teacher_router.get('/{course_id}/subscribers', status_code=200)
async def view_subscribers(user: user_dependency, course_id):
    if user is None or user.get('role').lower() == 'student':
        raise Unauthorized

    return await course_subscribers(user, course_id)

@teacher_router.delete('/{course_id}/subscriber/{subscriber_id}', status_code=200)
async def remove_subscriber(user: user_dependency, course_id, subscriber_id):
    if user is None or user.get('role').lower() == 'student':
        raise Unauthorized

    return await unsubscribe(user,course_id, subscriber_id)
