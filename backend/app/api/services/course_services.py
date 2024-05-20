from backend.app.data.database import insert_query, read_query, update_query
from backend.app.api.services.uploadpic_services import check_for_creator
from backend.app.api.utils.responses import NotFound
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


def switch_status(course_id: int, user_role: str, user_id: int):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student you cannot switch course status!")
    elif user_role == "teacher" and check_for_creator(user_id, course_id) or user_role == "admin":
        status_sql = "SELECT status FROM courses WHERE course_id = %s"
        execute = read_query(status_sql, (course_id,))
        status = execute[0][0]
        if status == "public":
            switch_sql = "UPDATE courses SET status = 'premium' WHERE course_id = %s"
            update_query(switch_sql, (course_id,))
            return {"message": "Course status switched to Premium"}
        switch_sql = "UPDATE courses SET status = 'public' WHERE course_id = %s"
        update_query(switch_sql, (course_id,))
        return {"message": "Course status switched to Public"}
    raise HTTPException(status_code=403, detail="You are not the creator of this course!")



