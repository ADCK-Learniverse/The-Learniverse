from backend.app.data.database import read_query, insert_query
from backend.app.models import User
from fastapi import HTTPException
import bcrypt


async def check_existing_email(email: str):
    return read_query("SELECT * FROM users WHERE email = %s", (email,))


async def register_user(user: User):
    if await check_existing_email(user.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    else:
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
        sql = ('INSERT INTO users(email,password,firstname,lastname, role, phone_number) '
               'VALUES (%s, %s, %s, %s, %s, %s)')
        insert_query(sql, (user.email, hashed_password, user.firstname,
                           user.lastname, user.role, user.phone_number))
        # await give_access_to_all_open_categories(user.email)
        return {"message": "User registered successfully"}



# async def give_access_to_all_open_categories(Username):
#     user_id = read_query('SELECT user_id FROM users WHERE username = %s', (Username,))
#     categories = read_query('SELECT category_id, is_open FROM category')
#
#     for cat_id, is_open in categories:
#         if is_open:
#             insert_query("INSERT INTO category_access (user_id, category_id, access_control) VALUES (%s, %s, %s)",
#                          (user_id[0][0], cat_id, 2))