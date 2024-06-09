from typing import Annotated, Optional
from fastapi import APIRouter, Depends

from backend.app.api.services.section_services import new_section, sections, section, remove_section
from backend.app.models import Section
from backend.app.api.services.login_services import get_current_user
user_dependency = Annotated[dict, Depends(get_current_user)]

section_router = APIRouter(prefix='/sections')


@section_router.post('/new', status_code=200)
async def create_section(user: user_dependency, section:Section):

    """This method uses the init method to create a new object with the inserted values for verifications
     and creates a new section inside the database with the values."""

    return await new_section(user, section)

@section_router.get('/', status_code=200)
async def all_sections(user: user_dependency, course_id: int, filter: Optional[str] = None):

    """This method returns all sections inside the specific course and provides the option to filter by id or name."""

    return await sections(user, course_id, filter)

@section_router.get('/{section_id}', status_code=200)
async def specific_section(user: user_dependency, section_id: int, course_id: int):

    """This method requires the id for the course and the section and returns the corresponding section."""

    return await section(user, section_id, course_id)

@section_router.delete('/{section_id}', status_code=200)
async def delete_section(user: user_dependency,course_id: int, section_id: int):

    """This method requires the id for the course and the section and deletes the corresponding section."""

    return await remove_section(user,course_id, section_id)


def section_related_endpoints(router: APIRouter):
    router.post('/', status_code=200)(create_section)
    router.get('/', status_code=200)(all_sections)
    router.get('/{section_id}', status_code=200)(specific_section)
    router.delete('/{section_id}', status_code=200)(delete_section)