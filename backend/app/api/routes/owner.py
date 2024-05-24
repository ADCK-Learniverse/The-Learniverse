from fastapi import APIRouter

from backend.app.api.routes.admin import admin_related_endpoints
from backend.app.api.routes.course import course_related_endpoints
from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.routes.section import section_related_endpoints
from backend.app.api.routes.teacher import teacher_related_endpoints

owner_router = APIRouter(prefix="/owner_panel")

@owner_router.get('')
async def home():
    return 'hello'

profile_related_endpoints(owner_router)
teacher_related_endpoints(owner_router)
admin_related_endpoints(owner_router)


