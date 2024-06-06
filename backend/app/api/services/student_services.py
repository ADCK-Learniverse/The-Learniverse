from backend.app import data
from fastapi import HTTPException
from backend.app.api.utils.utilities import format_user_info
from backend.app.api.services.course_services import view_particular


async def welcome_message(user_id: int):
    sql = "SELECT firstname FROM users WHERE user_id = %s"
    execute = data.database.read_query(sql, (user_id,))
    name = execute[0][0]
    return {"message": f"Hello, {name}"}


async def view_subscriptions(user_id: int, user_role: str, page: int = 1, size: int = 10):
    start = (page - 1) * size
    sql = "SELECT course_id FROM subscription WHERE user_id = %s LIMIT %s OFFSET %s"
    execute = await data.database.read_query(sql, (user_id, size, start))
    courses_count_sql = "SELECT COUNT(*) FROM subscription WHERE user_id = %s"
    courses_count = await data.database.read_query(courses_count_sql, (user_id,))[0][0]
    if not execute:
        raise HTTPException(status_code=404, detail="No subscriptions found!")
    course_ids = [row[0] for row in execute]
    subscribed_courses = []
    for course_id in course_ids:
        course_info = view_particular(course_id, user_id, user_role)
        subscribed_courses.append(course_info)
    return {
        f"Courses you're subscribed to: {courses_count}": subscribed_courses,
        "Page": page,
        "Size": size
    }

