from fastapi import UploadFile, File, HTTPException
from typing import Union
from backend.app.data.database import insert_query


def upload_picture(user_id: int, picture: Union[UploadFile, None] = File(None)):
    if picture is None:
        raise HTTPException(status_code=400, detail="No picture provided!")

    picture_content = picture.file.read()
    sql = "UPDATE users SET picture = %s WHERE user_id = %s"
    insert_query(sql, (picture_content, user_id))
    return {"message": "Profile picture updated."}