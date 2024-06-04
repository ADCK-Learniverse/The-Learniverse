import bcrypt
from starlette.responses import StreamingResponse, JSONResponse
import io

from backend.app import data
from backend.app.api.services.register_services import send_emails
from backend.app.api.utils.responses import NotFound
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
    user_info = format_user_info(execute)
    return {"User info": user_info}

def view_picture(user_id: int):
    info =  data.database.read_query('SELECT picture FROM users WHERE user_id = %s', (user_id,))
    if info:
        picture =  StreamingResponse(io.BytesIO(info[0][0]), media_type="image/png")
        return picture
    else:
        raise NotFound

def newsletter(email):
    info = data.database.read_query('SELECT * FROM newsletter WHERE email = %s', (email,))
    if info:
        return 'Already subscribed'
    data.database.insert_query('INSERT INTO newsletter(email) VALUES (%s)', (email,))

    send_emails(
        [email],
        "Testing Newsletter",
        "You have successfully subscribed to our newsletter",
        "<h3>I don't know what to write in here </h3>"
    )


def newsletter_subscribers():
    return data.database.read_query('SELECT email FROM newsletter')


