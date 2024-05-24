from backend.app.api.utils.responses import NoContent, NotFound, Unauthorized
from backend.app.api.utils.utilities import check_if_guest,check_if_student, format_section_details, \
    check_for_creator
from backend.app import data


async def new_section(user, section_data):
    check_if_guest(user)
    check_if_student(user)

    if check_for_creator(user_id=user.get('id'), course_id=section_data.course_id) == False:
        raise Unauthorized

    data.database.insert_query(
        'INSERT INTO sections(title, content, description,information, course_id) VALUES(%s,%s,%s,%s,%s)',
        (section_data.title, section_data.content,
         section_data.description, section_data.information, section_data.course_id))

    return {"message": "New Section created!"}


async def sections(user, course_id):
    check_if_guest(user)

    info = data.database.read_query('SELECT * FROM sections WHERE course_id = %s', (course_id,))
    if info:
        return format_section_details(info)

    else:
        raise NoContent


async def section(user, section_id, course_id):
    check_if_guest(user)

    info = data.database.read_query('SELECT * FROM sections WHERE section_id = %s AND course_id = %s',
                                    (section_id, course_id))
    if info:
        return format_section_details(info)

    else:
        raise NoContent


async def remove_section(user,course_id, section_id):
    check_if_guest(user)
    check_if_student(user)

    if check_for_creator(user_id=user.get('id'), course_id=course_id) == False:
        raise Unauthorized

    info = data.database.read_query('SELECT * FROM sections WHERE section_id = %s', (section_id,))
    if info:
        data.database.update_query('DELETE FROM sections WHERE section_id = %s', (section_id,))
        return {"message": "Section Deleted!"}

    else:
        raise NotFound
