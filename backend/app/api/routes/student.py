from fastapi import APIRouter

student_router = APIRouter(prefix="/student_panel")

@student_router.get('')
async def home():
    return 'hello'