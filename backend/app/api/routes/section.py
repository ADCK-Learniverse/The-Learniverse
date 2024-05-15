from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from backend.app.models import Section
from backend.app.api.services.login_services import get_current_user
from backend.app.api.utils.details import NOT_AUTHORIZED, RESTRICTED_ACCESS

user_dependency = Annotated[dict, Depends(get_current_user)]

section_router = APIRouter(prefix='/sections')


@section_router.post('/', status_code=200)
async def create_section(user: user_dependency, section:Section):
    if user is None:
        raise HTTPException(status_code=401, detail=NOT_AUTHORIZED)

