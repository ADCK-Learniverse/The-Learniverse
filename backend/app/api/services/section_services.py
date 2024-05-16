from backend.app.api.utils.responses import NoContent, NotFound
from backend.app.data.database import read_query, insert_query, update_query


async def new_section(section_data):
    insert_query('INSERT INTO sections(title, content, description,information, course_id) VALUES(%s,%s,%s,%s,%s)',
                 (section_data.title, section_data.content,
                  section_data.description, section_data.information, section_data.course_id))


    return 'New Section created'


async def sections():
    data = read_query('SELECT * FROM sections')
    if data:
        return format_section_details(data)

    else:
        raise NoContent


async def section(section_id):
    data = read_query('SELECT * FROM sections WHERE section_id = %s', (section_id,))
    if data:
        return format_section_details(data)

    else:
        raise NoContent


async def remove_section(section_id):
    if read_query('SELECT * FROM sections WHERE section_id = %s', (section_id,)):
        update_query('DELETE FROM sections WHERE section_id = %s', (section_id,))
        return "Section deleted"

    else:
        raise NotFound


def format_section_details(section_details_list):
    formatted_details = []
    for format_detail in section_details_list:
        formatted_details = {
            'Section Title': format_detail[1],
            'Section Content': format_detail[2],
            'Section Description': format_detail[3],
            'Section Information': format_detail[4],
            'Course Name': format_detail[5]
        }
    return formatted_details
