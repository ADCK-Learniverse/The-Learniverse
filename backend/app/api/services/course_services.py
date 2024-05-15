from backend.app.data.database import insert_query, read_query
from backend.app.models import Course
from fastapi import HTTPException


def new_course(user_id: int, user_role: str, course: Course):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student, you cannot create courses!")
    names_query = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    get_names = read_query(names_query, (user_id,))
    names = get_names[0][0] + " " + get_names[0][1]
    sql = ("INSERT INTO courses(title, description, objectives, owner, status, rating) VALUES"
           "(%s, %s, %s, %s, %s, %s)")
    insert_query(sql, (course.title, course.description, course.objectives,
                       names, course.status, course.rating))