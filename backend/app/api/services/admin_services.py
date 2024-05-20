from pydantic import Field
from backend.app.api.utils.utilities import check_if_student_or_guest, check_if_admin_or_owner
from backend.app.data.database import read_query, update_query



def get_user_by_id(user_id: int = Field(gt=0)):
    sql = "SELECT * FROM users WHERE user_id = %s"
    result = read_query(sql, (user_id,))
    return result

async def view_teacher_requests(user):

    check_if_admin_or_owner(user)

    data = read_query('SELECT * FROM users WHERE role = %s AND status = %s',
                      ('teacher', 'awaiting'))
    if data:
        return data
    else:
        return 'No pending requests'


async def deactivate(user, person_id):
    check_if_student_or_guest(user)
    update_query('UPDATE users SET status = %s WHERE user_id = %s', ('banned', person_id,))
    return 'User banned, access restricted'