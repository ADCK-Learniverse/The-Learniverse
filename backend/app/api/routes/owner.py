from fastapi import APIRouter

owner_router = APIRouter(prefix="/owner_panel")

@owner_router.get('')
async def home():
    return 'hello'