from fastapi import UploadFile, File, HTTPException
from typing import Union
from backend.app.data.database import insert_query, read_query


def update_user_picture(user_id: int, picture: Union[UploadFile, None] = File(None)):
    if picture is None:
        raise HTTPException(status_code=400, detail="No picture provided!")

    picture_content = picture.file.read()
    sql = "UPDATE users SET picture = %s WHERE user_id = %s"
    insert_query(sql, (picture_content, user_id))
    return {"message": "Profile picture updated."}


def update_course_picture(user_id: int, user_role: str, course_id: int, picture: Union[UploadFile, None] = File(None)):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student, you cannot update course pictures!")
    if picture is None:
        raise HTTPException(status_code=400, detail="No picture provided!")
    if not check_for_creator(user_id, course_id):
        raise HTTPException(status_code=403, detail="You are not the creator of this course!")
    picture_content = picture.file.read()
    sql = "UPDATE courses SET picture = %s WHERE course_id = %s"
    insert_query(sql, (picture_content, course_id))
    return {"message": "Course picture updated."}


def check_for_creator(user_id, course_id):
    course_names_sql = "SELECT owner FROM courses WHERE course_id = %s"
    execute_course = read_query(course_names_sql, (course_id,))
    course_owner = execute_course[0][0]
    names_sql = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    execute = read_query(names_sql, (user_id,))
    names = execute[0][0] + " " + execute[0][1]
    if names == course_owner:
        return True
    return False
