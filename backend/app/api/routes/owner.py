from typing import Annotated
from fastapi import APIRouter, Depends
from backend.app.api.routes.admin import admin_related_endpoints
from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.routes.teacher import teacher_related_endpoints
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.owner_services import convert

owner_router = APIRouter(prefix="/owner_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]

@owner_router.get('')
async def home():
    return 'hello'

profile_related_endpoints(owner_router)
teacher_related_endpoints(owner_router)
admin_related_endpoints(owner_router)


@owner_router.patch('/account_role', status_code=200)
async def account_role(user: user_dependency, person_email: str, role: str):
    """This method switches the account role of the selected user by selecting his email and one of the 3 existing roles"""
    return convert(user, person_email, role)

@owner_router.post('/token', status_code=201)
def take_info(user:user_dependency):
    information = {"username": user.get("sub"),
                   "role": user.get("role"),
                   "first": user.get('first_name'),
                   "last": user.get('last_name'),
                   "id": user.get('user_id')}

    return information

