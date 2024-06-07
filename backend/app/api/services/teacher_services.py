from backend.app.api.utils.utilities import (format_personal_information,
                                             format_subscription_details, check_owner, check_if_guest, check_if_student,
                                             format_requests)
from backend.app import data
from backend.app.api.utils.responses import NotFound, Unauthorized


async def course_subscribers(Teacher, course_id):
    check_if_guest(Teacher)
    check_if_student(Teacher)

    if Teacher.get('role').lower() == 'teacher' and check_owner(Teacher, course_id) is None:
        raise Unauthorized

    info = data.database.read_query("""
            SELECT subscription.course_id, subscription.user_id, CONCAT(users.firstname, ' ', users.lastname) AS fullname, courses.title
            FROM subscription
            INNER JOIN users ON users.user_id = subscription.user_id
            INNER JOIN courses ON courses.course_id = subscription.course_id
            WHERE subscription.course_id = %s;
            """, (course_id,))

    if not info:
        raise NotFound

    return format_subscription_details(info)


async def view_student_requests(user):
    check_if_guest(user)
    check_if_student(user)

    info = data.database.read_query('SELECT user_id,email,firstname,lastname,role,phone_number FROM users WHERE role = %s AND status = %s',
                                    ('student', 'awaiting'))
    if info:
        return format_requests(info)
    else:
        return 'No pending requests'