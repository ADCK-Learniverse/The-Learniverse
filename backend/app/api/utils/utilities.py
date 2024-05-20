from backend.app.api.utils.responses import Unauthorized
from backend.app.data.database import read_query, update_query


def format_personal_information(personal_details_list):

    formatted_details = {
        'Role': personal_details_list.get('role'),
        'Email': personal_details_list.get('email'),
        'First Name': personal_details_list.get('first name'),
        'Last Name': personal_details_list.get('last name'),
        'Phone Number': personal_details_list.get('phone number'),
    }
    return formatted_details

def format_subscription_details(subscription_details_List):
    formatted_details = []
    for n, format_detail in enumerate(subscription_details_List, start=1):
        formatted_details = {
            n: format_detail[2]
        }
    return {f'{subscription_details_List[0][3]} Subscribers': formatted_details}


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

def check_owner(Teacher, course_id):
    Teacher_name = f"{Teacher.get('first_name')} {Teacher.get('last_name')}"

    data = read_query('SELECT * FROM subscription WHERE course_id = %s AND owner = %s',
                      (course_id, Teacher_name))
    if data:
        return data

async def unsubscribe(Teacher, course_id, subscriber_id):
    if Teacher.get('role').lower() == 'teacher' and check_owner(Teacher, course_id) is None:
        raise Unauthorized

    update_query('DELETE FROM subscription WHERE course_id = %s AND user_id = %s',
                 (course_id,subscriber_id))
    return 'User unsubscribed successfully'


def format_course_info(content: list):
    return [
        {
            "Course Title": course[1],
            "Course ID": course[0],
            "Description": course[2],
            "Rating": course[3],
            "Status": course[4],
            "By": course[5],
            "Tags": course[6]
        }
        for course in content
    ]
