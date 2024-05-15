from fastapi import APIRouter, UploadFile, File
from pydantic import Field
from backend.app.api.services.uploadpic_services import upload_picture

picture_router = APIRouter(prefix="/profilepic")


@picture_router.post("/{user_id}", status_code=201)
def upload_pic(user_id: int, picture: UploadFile = File(...)):
    return upload_picture(user_id, picture)
