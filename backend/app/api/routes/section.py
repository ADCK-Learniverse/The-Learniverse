from typing import Annotated
from fastapi import APIRouter, Depends

from backend.app.api.services.section_services import new_section, sections, section, remove_section
from backend.app.models import Section
from backend.app.api.services.login_services import get_current_user
user_dependency = Annotated[dict, Depends(get_current_user)]

section_router = APIRouter(prefix='/sections')


@section_router.post('/', status_code=200)
async def create_section(user: user_dependency, section:Section):
    """This method creates a new section inside the selected course"""
    return await new_section(user, section)

@section_router.get('/', status_code=200)
async def all_sections(user: user_dependency, course_id: int):
    """This method returns all sections"""
    return await sections(user, course_id)

@section_router.get('/{section_id}', status_code=200)
async def specific_section(user: user_dependency, section_id: int, course_id: int):
    """This method returns a specific section from the desired course"""
    return await section(user, section_id, course_id)

@section_router.delete('/{section_id}', status_code=200)
async def delete_section(user: user_dependency, section_id: int):
    """This method deletes a specific section"""
    return await remove_section(user, section_id)
