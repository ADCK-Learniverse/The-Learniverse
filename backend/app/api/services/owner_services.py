from backend.app import data
from backend.app.api.utils.utilities import check_if_owner

def convert(user, person_id, role):
    check_if_owner(user)
    data.database.update_query('UPDATE users SET role = %s WHERE user_id = %s', (role, person_id))
    return f'Account role switched to {role}'




