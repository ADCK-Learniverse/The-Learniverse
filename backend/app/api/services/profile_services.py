import bcrypt
from backend.app import data
from backend.app.api.utils.utilities import format_user_info


def update_phone(user_id: int, new_number: str):
    sql = "UPDATE users SET phone_number = %s WHERE user_id = %s"
    data.database.update_query(sql, (new_number, user_id))
    return {"message": "Phone number updated!"}


def update_firstname(user_id: int, firstname: str):
    sql = "UPDATE users SET firstname = %s WHERE user_id = %s"
    data.database.update_query(sql, (firstname, user_id))
    return {"message": "First name updated!"}


def update_lastname(user_id: int, lastname: str):
    sql = "UPDATE users SET lastname = %s WHERE user_id = %s"
    data.database.update_query(sql, (lastname, user_id))
    return {"message": "Last name updated!"}

def update_password(user, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    data.database.update_query('UPDATE users SET password = %s WHERE user_id = %s', (hashed_password, user.get('id')))
    return {"message": "Password updated!"}


def view_profile(user_id: int):
    sql = "SELECT firstname, lastname, email, phone_number, role, status FROM users WHERE user_id = %s"
    execute = data.database.read_query(sql, (user_id,))
    return {"User info": format_user_info(execute)}

def newsletter(email):
    info = data.database.read_query('SELECT * FROM newsletter WHERE email = %s', (email,))
    if info:
        return 'Already subscribed'
    data.database.insert_query('INSERT INTO newsletter(email) VALUES (%s)', (email,))
    return "Successfully subscribed to newsletter"



