from fastapi import HTTPException
from pydantic import Field

from backend.app import data
from backend.app.api.utils.utilities import check_if_guest, check_if_student,check_if_teacher,check_if_admin
def promote(user, user_id: int = Field(..., gt=0)):
    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)
    check_if_admin(user)

    info = data.database.read_query('SELECT * FROM users '
                      'WHERE user_id = %s AND role != %s', (user_id, 'admin'))
    if any(info):
        data.database.update_query('UPDATE users SET role = %s WHERE user_id = %s', ('admin', user_id))
        return {"message": ['User Promoted']}
    else:
        raise HTTPException(status_code=404,
                            detail=f'This Account is already an Admin or Account with ID {user_id} does not exist')


def demote(user, user_id: int = Field(..., gt=0)):
    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)
    check_if_admin(user)


    info =  data.database.read_query('SELECT * FROM users '
                      'WHERE user_id = %s AND role = %s', (user_id, 'admin'))
    if any(info):
        data.database.update_query('UPDATE users SET role = %s WHERE user_id = %s', ('user', user_id))
        return {"message": ['User Demoted']}
    else:
        raise HTTPException(status_code=404,
                            detail=f'This Account is not an Admin or Account with ID {user_id} does not exist')


def delete_admin_account(user, admin_id: int = Field(..., gt=0)):
    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)
    check_if_admin(user)

    info =  data.database.read_query('SELECT * FROM users '
                      'WHERE user_id = %s AND role = %s', (admin_id, 'admin'))
    if any(info):
        data.database.update_query((
            f"UPDATE users "
            f"SET email = 'Default{admin_id}', "
            f"password = 'NULL', "
            f"firstname = NULL, "
            f"lastname = NULL, "
            f"role = NULL, "
            f"phone_number = NULL,"
            f"other_accounts = NULL, "
            f"picture = NULL, "
            f"status = NULL"

            f"WHERE user_id = %s"), (admin_id,))
        return {'message': ['User deleted successfully!']}
    else:
        raise HTTPException(status_code=404,
                            detail=f'This Account is not an Admin or does not exist!')