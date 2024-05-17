from fastapi import APIRouter

admin_router = APIRouter(prefix="/admin_panel")

@admin_router.get('')
async def home():
    return 'hello'