from random import randrange

from backend.app.api.utils.responses import NotFound
from backend.app.data.database import insert_query, read_query, update_query
from backend.app.models import User
from fastapi import HTTPException
import bcrypt
import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()


async def check_existing_email(email: str):
    return read_query("SELECT * FROM users WHERE email = %s", (email,))


def get_emails_by_role(role: str):
    sql = "SELECT email FROM users WHERE role = %s"
    result = read_query(sql, (role,))
    return [row[0] for row in result]


def send_emails(emails: list, subject: str, text_part: str, html_part: str):
    api_key_public = os.getenv('MJ_APIKEY_PUBLIC')
    api_key_private = os.getenv('MJ_APIKEY_PRIVATE')

    if not api_key_public or not api_key_private:
        raise HTTPException(status_code=500, detail="Mailjet API keys are not set")

    messages = [
        {
            "From": {
                "Email": "kostadinovchavdar@gmail.com",
                "Name": "The Learniverse"
            },
            "To": [{"Email": email} for email in emails],
            "Subject": subject,
            "TextPart": text_part,
            "HTMLPart": html_part
        }
    ]

    payload = {
        "Messages": messages
    }

    response = requests.post(
        "https://api.mailjet.com/v3.1/send",
        auth=(api_key_public, api_key_private),
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send email notifications")


async def student(user: User):
    if await check_existing_email(user.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    else:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        sql = ('INSERT INTO users(email,password,firstname,lastname, role, phone_number) '
               'VALUES (%s, %s, %s, %s, %s, %s)')
        insert_query(sql, (user.email, hashed_password, user.firstname,
                           user.lastname, 'student', user.phone_number))

        teacher_emails = get_emails_by_role('teacher')
        send_emails(
            teacher_emails,
            "New Student Registration",
            "A new student is waiting to be approved.",
            "<h3>A new student is waiting to be approved.</h3>"
        )

        return {"message": "Student registered successfully"}


async def teacher(user: User):
    if await check_existing_email(user.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    else:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        sql = ('INSERT INTO users(email,password,firstname,lastname, role, phone_number) '
               'VALUES (%s, %s, %s, %s, %s, %s)')
        insert_query(sql, (user.email, hashed_password, user.firstname,
                           user.lastname, 'teacher', user.phone_number))

        admin_emails = get_emails_by_role('admin')
        send_emails(
            admin_emails,
            "New Teacher Registration",
            "A new teacher is waiting to be approved.",
            "<h3>A new teacher is waiting to be approved.</h3>"
        )

        return {"message": "Teacher registered successfully"}

async def generate_new_password(email):
    info =  read_query('SELECT email FROM users WHERE email = %s', (email,))
    generated_password = str(randrange(10000, 800000000))
    new_password = bcrypt.hashpw(generated_password.encode('utf-8'), bcrypt.gensalt())


    if info:
        update_query('UPDATE users SET password = %s WHERE email = %s', (new_password, email))
        send_emails(
            [info[0][0]],
            "Password recovery",
            "Password recovery.",
            f"<h3>This email contains your new password {generated_password} it will be active for the next 15 min, after"
            f" you log in, go inside your Profile page and update your password</h3>"
        )
        return {"message": "Password changed successfully"}
    raise NotFound

