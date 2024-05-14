from starlette.responses import HTMLResponse


from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

from backend.app.api.services.register_services import register_user

register_router = APIRouter(prefix='/register')
templates = Jinja2Templates(directory="frontend")


# @register_router.post('', status_code=201)
# async def register(user: User):
#     """
#     This method takes the user's data required for a registration and adds them to the database
#     as a registered user
#     """
#     return await register_user(user)


@register_router.get('/')
async def register_page(request: Request):
    """
    Render the registration page with a form for user registration
    """
    return templates.TemplateResponse("register_page.html", {"request": request})

@register_router.post('/register_user', status_code=201)
async def register_user_form(user: User):
    """
    Process the submitted user registration form
    """
    await register_user(user)
    return {"message": "User registered successfully"}