from backend.app.api.utils.utilities import format_personal_information, format_subscription_details, check_owner
from backend.app.data.database import read_query, update_query
from backend.app.api.utils.responses import NotFound, Unauthorized


async def get_information(user):
    return format_personal_information(user)


async def update_information(user_id, update):
    first_name = update.First_name
    last_name = update.Last_name
    phone_number = update.Phone_number
    password = update.Password

    if first_name != 'string':
        update_query('UPDATE users SET firstname = %s WHERE user_id = %s',
                     (first_name, user_id))

    if last_name != 'string':
        update_query('UPDATE users SET lastname = %s WHERE user_id = %s',
                     (last_name, user_id))

    if phone_number != 'string':
        update_query('UPDATE users SET phone_number = %s WHERE user_id = %s',
                     (phone_number, user_id))
    # write update password

    return 'Profile Update successfully'


async def course_subscribers(Teacher, course_id):
    if Teacher.get('role').lower() == 'teacher' and check_owner(Teacher, course_id) is None:
        raise Unauthorized

    data = read_query("""
            SELECT subscription.course_id, subscription.user_id, CONCAT(users.firstname, ' ', users.lastname) AS fullname, courses.title
            FROM subscription
            INNER JOIN users ON users.user_id = subscription.user_id
            INNER JOIN courses ON courses.course_id = subscription.course_id
            WHERE subscription.course_id = %s;
            """, (course_id,))

    if not data:
        raise NotFound

    return format_subscription_details(data)







