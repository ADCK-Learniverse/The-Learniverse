from backend.app.data.database import insert_query, read_query, update_query
from backend.app.api.services.uploadpic_services import check_for_creator
from backend.app.models import Course
from fastapi import HTTPException
from pydantic import Field
from backend.app.api.utils.utilities import format_course_info


def new_course(user_id: int, user_role: str, course: Course):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student, you cannot create courses!")
    if check_for_existing_course(course.title):
        raise HTTPException(status_code=409, detail="A course with this title already exists!")
    names_query = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    get_names = read_query(names_query, (user_id,))
    names = get_names[0][0] + " " + get_names[0][1]
    joined_tags = ",".join(course.tags)
    sql = ("INSERT INTO courses(title, description, objectives, owner, status, rating, tags) VALUES"
           "(%s, %s, %s, %s, %s, %s, %s)")
    insert_query(sql, (course.title, course.description, course.objectives,
                       names, course.status, course.rating, joined_tags))
    return {"message": "Course created successfully!"}


def delete_course(user_id: int, user_role: str, course_id: int):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student you cannot delete courses!")
    if check_for_creator(user_id, course_id) or user_role == "admin":
        delete_sql = "DELETE FROM courses WHERE course_id = %s"
        update_query(delete_sql, (course_id,))
        return {"message": "Course deleted!"}


def view_all():
    sql = "SELECT course_id, title, description, rating, status, owner, tags FROM courses"
    execute = read_query(sql)
    return format_course_info(execute)


def check_for_existing_course(title: str):
    sql = "SELECT * FROM courses WHERE title = %s"
    return read_query(sql, (title, ))


def view_particular(course_id: int):
    sql = "SELECT course_id, title, description, rating, status, owner, tags FROM courses WHERE course_id = %s"
    execute = read_query(sql, (course_id,))
    if not execute:
        raise HTTPException(status_code=404, detail="Course not found!")
    return format_course_info(execute)


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

def subscribe(user_id: int = Field(gt=0), course_id: int = Field(gt=0)):
    subscription_sql = "INSERT INTO subscription(course_id, user_id) VALUES (%s, %s)"
    insert_query(subscription_sql, (course_id, user_id))
    return {"message": "You have subscribed to this course!"}


def unsubscribe(user_id: int = Field(gt=0), course_id: int = Field(gt=0)):
    remove_sub_sql = "DELETE FROM subscription WHERE user_id = %s AND course_id = %s"
    update_query(remove_sub_sql, (user_id, course_id))
    return {"message": "You have removed your subscription!"}


def rate(user_id: int = Field(gt=0), course_id: int = Field(gt=0), rating: int = Field(gt=0, lt=11)):
    if check_for_creator(user_id, course_id):
        raise HTTPException(status_code=403, detail="You cannot rate your own courses!")
    sql = "INSERT INTO course_rating(user_id, course_id, rating) VALUES (%s, %s, %s)"
    insert_query(sql, (user_id, course_id, rating))
    update_course_rating(course_id, rating)
    return {"message": f"You have rated this course {rating} out of 10!"}


def update_course_rating(course_id: int, rating: int):
    rates_sql = "SELECT COUNT(*), SUM(rating) FROM course_rating WHERE course_id = %s"
    execute_rates_sql = read_query(rates_sql, (course_id,))
    ratings = int(execute_rates_sql[0][0])
    total_rating_value = int(execute_rates_sql[0][1])
    print(total_rating_value)
    calculate_rating = float(total_rating_value / (ratings * 10)) * 10
    calculation_sql = "UPDATE courses SET rating = %s WHERE course_id = %s"
    update_query(calculation_sql, (calculate_rating, course_id))
