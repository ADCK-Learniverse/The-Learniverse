from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.api.routes.admin import admin_related_endpoints
from backend.app.api.routes.course import course_related_endpoints
from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.routes.section import section_related_endpoints
from backend.app.api.routes.teacher import teacher_related_endpoints
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.owner_services import promote, demote, delete_admin_account

owner_router = APIRouter(prefix="/owner_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]

@owner_router.get('')
async def home():
    return 'hello'

profile_related_endpoints(owner_router)
teacher_related_endpoints(owner_router)
admin_related_endpoints(owner_router)


@owner_router.put('/promote/{user_id}', status_code=201)
async def create_admin(user: user_dependency, user_id: int):
    """
    This method takes the desired ID and turns the corresponding user into an ADMIN.
    """
    return await promote(user, user_id)



@owner_router.put('/demote/{user_id}', status_code=201)
async def demote_admin(user: user_dependency, user_id: int):
    """
    This method takes the desired ID and strips the corresponding user from his ADMIN rights.
    """

    return await demote(user, user_id)



@owner_router.delete(path='/{admin_id}', status_code=204)
async def delete_admin(user: user_dependency, admin_id: int):
    """
    This method takes the desired ID, checks for any matches,
    and if found it entirely removed the user.
    """

    return await delete_admin_account(user, admin_id)


