from backend.app.api.utils.responses import NoContent, NotFound
from backend.app.api.utils.utilities import format_section_details, check_if_student_or_guest, check_if_guest
from backend.app.data.database import read_query, insert_query, update_query


async def new_section(user, section_data):
    check_if_student_or_guest(user)

    insert_query('INSERT INTO sections(title, content, description,information, course_id) VALUES(%s,%s,%s,%s,%s)',
                 (section_data.title, section_data.content,
                  section_data.description, section_data.information, section_data.course_id))


    return 'New Section created'


async def sections(user):
    check_if_guest(user)

    data = read_query('SELECT * FROM sections')
    if data:
        return format_section_details(data)

    else:
        raise NoContent


async def section(user, section_id):
    check_if_guest(user)


    data = read_query('SELECT * FROM sections WHERE section_id = %s', (section_id,))
    if data:
        return format_section_details(data)

    else:
        raise NoContent


async def remove_section(user, section_id):
    check_if_student_or_guest(user)


    if read_query('SELECT * FROM sections WHERE section_id = %s', (section_id,)):
        update_query('DELETE FROM sections WHERE section_id = %s', (section_id,))
        return "Section deleted"

    else:
        raise NotFound

