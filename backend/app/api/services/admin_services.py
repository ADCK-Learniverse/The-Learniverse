from pydantic import Field
from backend.app.api.utils.utilities import check_if_guest, check_if_student, check_if_teacher, format_requests
from backend.app import data



def get_user_by_id(user_id: int = Field(gt=0)):
    sql = "SELECT * FROM users WHERE user_id = %s"
    result = data.database.read_query(sql, (user_id,))
    return result

async def view_teacher_requests(user):

    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)

    info = data.database.read_query('SELECT user_id,email,firstname,lastname,phone_number FROM users WHERE role = %s AND status = %s',
                      ('teacher', 'awaiting'))
    if info:
        return format_requests(info)
    else:
        return {"message": "'No pending requests"}


async def deactivate(user, person_id):
    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)


    data.database.update_query('UPDATE users SET status = %s WHERE user_id = %s', ('banned', person_id,))
    return {"message": "User banned, access restricted"}