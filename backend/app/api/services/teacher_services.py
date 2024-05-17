from backend.app.api.utils.utilities import format_personal_information
from backend.app.data.database import read_query, update_query


async def get_information(user):
    return format_personal_information(user)



async def update_information(user_id, update):
    first_name = update.First_name
    last_name = update.Last_name
    phone_number = update.Phone_number
    password = update.Password

    if first_name != 'string':
        update_query('UPDATE users SET firstname = %s WHERE user_id = %s',
                     (first_name, user_id))

    if last_name != 'string':
            update_query('UPDATE users SET lastname = %s WHERE user_id = %s',
                         (last_name, user_id))

    if phone_number != 'string':
            update_query('UPDATE users SET phone_number = %s WHERE user_id = %s',
                         (phone_number, user_id))
    # write password

    return 'Profile Update successfully'




