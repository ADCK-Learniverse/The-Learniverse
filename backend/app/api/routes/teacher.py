from fastapi import APIRouter
from backend.app.api.routes.course import create_course

teacher_router = APIRouter(prefix='/teacher_panel')

