from typing import Annotated

from fastapi import APIRouter, Depends
from backend.app.api.routes.course import create_course
from backend.app.api.services.login_services import get_current_user
from backend.app.api.utils.responses import Unauthorized
from backend.app.api.services.teacher_services import get_information, update_information
from backend.app.models import UpdateProfile

teacher_router = APIRouter(prefix='/teacher_panel')

user_dependency = Annotated[dict, Depends(get_current_user)]
# information = user_dependency[0]
@teacher_router.get('/', status_code=200)
async def account_information(user: user_dependency):

    if user is None or user.get('role') != 'Teacher':
        raise Unauthorized

    return await get_information(user)



@teacher_router.patch('/teacher', status_code=200)
async def update_personal_information(user: user_dependency, update: UpdateProfile):
    if user is None or user.get('role') != 'Teacher':
        raise Unauthorized

    return await update_information(user.get('id'), update)

