from starlette.responses import HTMLResponse


from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates
from backend.app.models import User
from backend.app.api.services.register_services import student, teacher, generate_new_password

register_router = APIRouter(prefix='/register')
templates = Jinja2Templates(directory="frontend")


@register_router.post('/student', status_code=201)
async def register_student(user: User):
    """
    This method takes the user's data required for registration
    and adds them to the database as a registered student with awaiting status.
    """
    return await student(user)

@register_router.post('/teacher', status_code=201)
async def register_teacher(user: User):
    """
    This method takes the user's data required for registration
    and adds them to the database as a registered teacher with awaiting status.
    """
    return await teacher(user)


@register_router.post('/recover_password', status_code=200)
async def password_recovery(email:str):
    return await generate_new_password(email)
