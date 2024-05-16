from typing import Annotated
from fastapi import APIRouter, Depends

from backend.app.api.services.section_services import new_section, sections, section, remove_section
from backend.app.api.utils.responses import Unauthorized
from backend.app.models import Section
from backend.app.api.services.login_services import get_current_user
user_dependency = Annotated[dict, Depends(get_current_user)]

section_router = APIRouter(prefix='/sections')


@section_router.post('/', status_code=200)
async def create_section(user: user_dependency, section:Section):
    if user is None or user.get('role') == 'student':
        raise Unauthorized


    return await new_section(section)

@section_router.get('/', status_code=200)
async def all_sections(user: user_dependency):
    if user is None:
        raise Unauthorized


    return await sections()

@section_router.get('/{section_id}', status_code=200)
async def specific_section(user: user_dependency, section_id):
    if user is None:
        raise Unauthorized


    return await section(section_id)

@section_router.delete('/{section_id}', status_code=200)
async def delete_section(user: user_dependency, section_id):
    if user is None or user.get('role') == 'student':
        raise Unauthorized


    return await remove_section(section_id)
