from backend.app import data
from backend.app.api.utils.utilities import check_if_owner

def convert(user, person_email, role):
    check_if_owner(user)
    data.database.update_query('UPDATE users SET role = %s WHERE email = %s', (role, person_email))
    return f'Account role switched to {role}'




