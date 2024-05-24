from backend.app.api.utils.utilities import check_for_creator
from backend.app import data
from PIL import Image
import io
from fastapi import HTTPException, UploadFile, File
from typing import Union


def compress_image(image_content: bytes, max_size_mb: int = 5) -> bytes:
    image = Image.open(io.BytesIO(image_content))
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    compressed_image_io = io.BytesIO()
    quality = 85
    while True:
        compressed_image_io.seek(0)
        image.save(compressed_image_io, format='JPEG', quality=quality)
        size = compressed_image_io.tell()
        if size <= max_size_mb * 1024 * 1024:
            break
        quality -= 5
        if quality <= 0:
            raise HTTPException(status_code=500, detail="Cannot compress the image to the required size!")
    compressed_image_io.seek(0)
    compressed_image_content = compressed_image_io.read()

    return compressed_image_content


def update_user_picture(user_id: int, picture: Union[UploadFile, None] = File(None)):
    if picture is None:
        raise HTTPException(status_code=400, detail="No picture provided!")
    picture_content = picture.file.read()
    compressed_picture_content = compress_image(picture_content)
    sql = "UPDATE users SET picture = %s WHERE user_id = %s"
    data.database.insert_query(sql, (compressed_picture_content, user_id))
    return {"message": "Profile picture updated."}


def update_course_picture(user_id: int, user_role: str, course_id: int, picture: Union[UploadFile, None] = File(None)):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student, you cannot update course pictures!")
    if picture is None:
        raise HTTPException(status_code=400, detail="No picture provided!")
    if not check_for_creator(user_id, course_id):
        raise HTTPException(status_code=403, detail="You are not the creator of this course!")

    picture_content = picture.file.read()

    compressed_picture_content = compress_image(picture_content)

    sql = "UPDATE courses SET picture = %s WHERE course_id = %s"
    data.database.insert_query(sql, (compressed_picture_content, course_id))

    return {"message": "Course picture updated."}


