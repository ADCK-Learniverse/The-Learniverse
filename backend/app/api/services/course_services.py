import base64

from backend.app import data
from backend.app.api.services.uploadpic_services import check_for_creator
from backend.app.api.services.section_services import sections
from backend.app.api.utils.newsletter_utilities import new_course_newsletter, removed_course_newsletter
from backend.app.api.utils.utilities import format_ratings, format_course_info, get_course_sections
from backend.app.models import Course
from fastapi import HTTPException
from pydantic import Field


def new_course(user_id: int, user_role: str, course: Course):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student, you cannot create courses!")
    if not check_if_user_is_approved(user_id):
        raise HTTPException(status_code=403, detail="In order to create a course, you must be approved first!")
    if check_for_existing_course(course.title):
        raise HTTPException(status_code=409, detail="A course with this title already exists!")
    names_query = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    get_names = data.database.read_query(names_query, (user_id,))
    names = get_names[0][0] + " " + get_names[0][1]
    joined_tags = ", ".join(course.tags)
    sql = ("INSERT INTO courses(title, description, objectives, owner, status, tags) VALUES"
           "(%s, %s, %s, %s, %s, %s)")
    data.database.insert_query(sql, (course.title, course.description, course.objectives,
                                     names, course.status, joined_tags))


    new_course_newsletter(course.title) # Send Email notifications to the subscribed users
    return {"message": "Course created successfully!"}


def delete_course(user_id: int, user_role: str, course_id: int):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student you cannot delete courses!")
    if check_for_creator(user_id, course_id) or user_role == "admin" or user_role == "owner":
        delete_sql = "DELETE FROM courses WHERE course_id = %s"
        data.database.update_query(delete_sql, (course_id,))

        removed_course_newsletter()
        return {"message": "Course deleted!"}
    raise HTTPException(status_code=403, detail="You are not the creator of this course!")


def view_all(search, page=1, size=10):
    start = (page - 1) * size
    if not search:
        sql = "SELECT course_id, title, description, rating, status, owner, tags FROM courses"
    elif isinstance(search, str):
        sql = ("SELECT course_id, title, description, rating, status, owner, tags FROM courses"
               " WHERE FIND_IN_SET(%s, tags) > 0")

    sql += " LIMIT %s OFFSET %s"

    if not search:
        execute = data.database.read_query(sql, (size, start))
        courses = format_course_info(execute)
    elif isinstance(search, str):
        execute = data.database.read_query(sql, (search, size, start))
        courses = format_course_info(execute)
    return {
        "Courses": courses,
        "Page": page,
        "Size": size
    }


def check_for_existing_course(title: str):
    sql = "SELECT * FROM courses WHERE title = %s"
    return  data.database.read_query(sql, (title, ))




def view_particular(course_id: int, user_id: int, user_role: str):
    if not check_if_user_is_approved(user_id):
        raise HTTPException(status_code=403, detail="You must be approved in order to view courses!")
    if user_role == "student":
        if check_course_status(course_id) == "premium" and not check_for_subscription(user_id, course_id):
            raise HTTPException(status_code=403, detail="You must be subscribed in order to see this course!")
    course_sql = "SELECT course_id, title, description, rating, status, owner, tags, picture FROM courses WHERE course_id = %s"
    execute = data.database.read_query(course_sql, (course_id,))
    if not execute:
        raise HTTPException(status_code=404, detail="Course not found!")
    course_format = format_course_info(execute)
    sections_check = get_course_sections(course_id)
    if sections_check:
        course_format[0]["Sections"] = sections_check
        visited_sections_sql = "SELECT visited_sections FROM users WHERE user_id = %s"

        visited_sections_data = data.database.read_query(visited_sections_sql, (user_id,))
        visited_sections_str = visited_sections_data[0][0]
        visited_sections = set(map(int, visited_sections_str.split(','))) if visited_sections_str else set()

        total_sections = len(sections_check)
        visited_count = sum(1 for section in sections_check if section['Section ID'] in visited_sections)
        progress_percentage = (visited_count / total_sections) * 100 if total_sections > 0 else 0

        course_format[0]['Progress'] = f"{progress_percentage:.2f}%"

        image_data = get_pic_for_frontend(course_id)
        if image_data:
            course_format[0]["picture"] = image_data["picture"]

        return course_format
    else:
        return course_format

def switch_status(course_id: int, user_role: str, user_id: int):
    if user_role == "student":
        raise HTTPException(status_code=403, detail="As a student you cannot switch course status!")
    elif user_role == "teacher" and check_for_creator(user_id, course_id) or user_role == "admin":
        status_sql = "SELECT status FROM courses WHERE course_id = %s"
        execute = data.database.read_query(status_sql, (course_id,))
        status = execute[0][0]
        if status == "public":
            switch_sql = "UPDATE courses SET status = 'premium' WHERE course_id = %s"
            data.database.update_query(switch_sql, (course_id,))
            return {"message": "Course status switched to Premium"}
        switch_sql = "UPDATE courses SET status = 'public' WHERE course_id = %s"
        data.database.update_query(switch_sql, (course_id,))
        return {"message": "Course status switched to Public"}
    raise HTTPException(status_code=403, detail="You are not the creator of this course!")


def subscribe(user_id: int = Field(gt=0), course_id: int = Field(gt=0)):
    if check_for_subscription(user_id, course_id):
        raise HTTPException(status_code=403, detail="You already subscribed to this course!")
    if not check_if_user_is_approved(user_id):
        raise HTTPException(status_code=403, detail="You must be approved in order to subscribe to courses")
    if check_course_status(course_id) == "premium":
        if count_premiums(user_id) == 5:
            raise HTTPException(status_code=403, detail="You can't subscribe to more than 5 premium courses")
        status = check_course_status(course_id)
        subscription_sql = "INSERT INTO subscription(course_id, user_id, course_status) VALUES (%s, %s, %s)"
        data.database.insert_query(subscription_sql, (course_id, user_id, status))
        return {"message": "You have subscribed to this course!"}
    status = check_course_status(course_id)
    subscription_sql = "INSERT INTO subscription(course_id, user_id, course_status) VALUES (%s, %s, %s)"
    data.database.insert_query(subscription_sql, (course_id, user_id, status))
    return {"message": "You have subscribed to this course!"}


def unsubscribe(user_id: int = Field(gt=0), course_id: int = Field(gt=0)):
    remove_sub_sql = "DELETE FROM subscription WHERE user_id = %s AND course_id = %s"
    data.database.update_query(remove_sub_sql, (user_id, course_id))
    return {"message": "You have removed your subscription!"}


def rate(user_id: int = Field(gt=0), course_id: int = Field(gt=0), rating: int = Field(gt=0, lt=11)):
    if not check_for_subscription(user_id, course_id):
        raise HTTPException(status_code=403, detail="You cannot rate courses you aren't subscribed to!")
    if check_for_creator(user_id, course_id):
        raise HTTPException(status_code=403, detail="You cannot rate your own courses!")
    if check_for_rating(user_id, course_id):
        raise HTTPException(status_code=403, detail="You have already rated this course!")

    sql = "INSERT INTO course_rating(user_id, course_id, rating) VALUES (%s, %s, %s)"
    data.database.insert_query(sql, (user_id, course_id, rating))
    update_course_rating(course_id, rating)
    return {"message": f"You have rated this course {rating} out of 10!"}


def update_course_rating(course_id: int, rating: int):
    rates_sql = "SELECT COUNT(*), SUM(rating) FROM course_rating WHERE course_id = %s"
    execute_rates_sql = data.database.read_query(rates_sql, (course_id,))
    ratings = int(execute_rates_sql[0][0])
    total_rating_value = int(execute_rates_sql[0][1])
    print(total_rating_value)
    calculate_rating = float(total_rating_value / (ratings * 10)) * 10
    calculation_sql = "UPDATE courses SET rating = %s WHERE course_id = %s"
    data.database.update_query(calculation_sql, (calculate_rating, course_id))


def check_for_subscription(user_id: int, course_id: int):
    sql = "SELECT * FROM subscription WHERE user_id = %s AND course_id = %s"
    execute = data.database.read_query(sql, (user_id, course_id))
    if execute:
        return execute
    else:
        return None


def check_if_user_is_approved(user_id: int):
    sql = "SELECT status FROM users WHERE user_id = %s"
    execute = data.database.read_query(sql, (user_id,))
    if execute[0][0] != "approved":
        return False
    return True


def check_course_status(course_id: int):
    sql = "SELECT status FROM courses WHERE course_id = %s"
    execute = data.database.read_query(sql, (course_id,))
    return execute[0][0]


def show_ratings(course_id: int, page: int = 1, size: int = 10):
    start = (page - 1) * size

    total_ratings_sql = "SELECT COUNT(*) FROM course_rating WHERE course_id = %s"
    total_ratings = data.database.read_query(total_ratings_sql, (course_id,))[0][0]

    sql = "SELECT user_id, rating FROM course_rating WHERE course_id = %s LIMIT %s OFFSET %s"
    execute = data.database.read_query(sql, (course_id, size, start))
    ratings = format_ratings(execute)

    return {
        "Ratings": ratings,
        "Total Ratings": total_ratings,
        "Page": page,
        "Size": size
    }


def count_premiums(user_id: int):
    sql = "SELECT COUNT(*) FROM subscription WHERE user_id = %s AND course_status = 'premium'"
    execute = data.database.read_query(sql, (user_id,))
    return execute[0][0]


def check_for_rating(user_id: int, course_id: int):
    sql = "SELECT * FROM course_rating WHERE user_id = %s AND course_id = %s"
    execute = data.database.read_query(sql, (user_id, course_id,))
    return execute


def get_pic_for_frontend(course_id: int):
    sql = "SELECT picture FROM courses WHERE course_id = %s"
    picture = data.database.read_query(sql, (course_id,))
    if picture:
        picture_blob = picture[0][0]
        if picture_blob is not None:
            base64_picture = base64.b64encode(picture_blob).decode('utf-8')
            base64_picture = f"data:image/jpeg;base64,{base64_picture}"
            return {"picture": base64_picture}

    return {"picture": None}
