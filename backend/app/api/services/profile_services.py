import bcrypt
from starlette.responses import StreamingResponse, JSONResponse
import io
import base64
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
    image_data = get_pic_for_frontend(user_id)

    if image_data:
        user_info[0]["picture"] = image_data["picture"]
    return {"User info": user_info}


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


def get_pic_for_frontend(user_id: int):
    sql = "SELECT picture FROM users WHERE user_id = %s"
    result = data.database.read_query(sql, (user_id,))

    picture_blob = result[0][0]
    if picture_blob:
        base64_picture = base64.b64encode(picture_blob).decode('utf-8')
        base64_picture = f"data:image/jpeg;base64,{base64_picture}"

        return {"picture": base64_picture}
    return {"picture": None}

