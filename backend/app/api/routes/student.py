from fastapi import APIRouter

student_router = APIRouter(prefix="/admin_panel")

@student_router.get('')
async def home():
    return 'hello'