from backend.app.api.utils.utilities import (format_personal_information,
                                             format_subscription_details, check_owner, check_if_guest, check_if_student,
                                             format_requests)
from backend.app import data
from backend.app.api.utils.responses import NotFound, Unauthorized


# async def get_information(user):
#     check_if_student_or_guest(user)
#
#     return format_personal_information(user)
#

# async def update_information(user, update):
#     check_if_student_or_guest(user)
#     user_id = user.get('id')
#     first_name = update.First_name
#     last_name = update.Last_name
#     phone_number = update.Phone_number
#     password = update.Password
#
#     if first_name != 'string':
#         data.database.update_query('UPDATE users SET firstname = %s WHERE user_id = %s',
#                                    (first_name, user_id))
#
#     if last_name != 'string':
#         data.database.update_query('UPDATE users SET lastname = %s WHERE user_id = %s',
#                                    (last_name, user_id))
#
#     if phone_number != 'string':
#         data.database.update_query('UPDATE users SET phone_number = %s WHERE user_id = %s',
#                                    (phone_number, user_id))
#     # write update password
#
#     return 'Profile Update successfully'


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

    info = data.database.read_query('SELECT email,firstname,lastname,role,phone_number FROM users WHERE role = %s AND status = %s',
                                    ('student', 'awaiting'))
    if info:
        return format_requests(info)
    else:
        return 'No pending requests'