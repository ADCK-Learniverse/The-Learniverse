from backend.app.api.utils.responses import Unauthorized
from backend.app import data


def format_personal_information(personal_details_list):
    """This method formats the personal information of the user."""

    formatted_details = {
        'Role': personal_details_list.get('role'),
        'Email': personal_details_list.get('email'),
        'First Name': personal_details_list.get('first name'),
        'Last Name': personal_details_list.get('last name'),
        'Phone Number': personal_details_list.get('phone number'),
    }
    return formatted_details


def format_subscription_details(subscription_details_List):
    """This method formats the subscription information list of all users subscribed to the course."""

    formatted_details = []
    for n, format_detail in enumerate(subscription_details_List, start=1):
        formatted_details = {
            n: format_detail[2]
        }
    return {f'{subscription_details_List[0][3]} Subscribers': formatted_details}


def format_section_details(section_details_list):
    """This method formats the section information list."""
    return [{
            'Section Title': format_detail[1],
            'Section Content': format_detail[2],
            'Section Description': format_detail[3],
            'Section Information': format_detail[4],
            'Course Name': format_detail[5]
        } for format_detail in section_details_list ]



def check_owner(Teacher, course_id):
    """This method checks if the Teacher is the owner of the course."""

    Teacher_name = f"{Teacher.get('first_name')} {Teacher.get('last_name')}"

    info = data.database.read_query('SELECT * FROM courses WHERE course_id = %s AND owner = %s',
                      (course_id, Teacher_name))
    if info:
        return info


async def unsubscribe(Teacher, course_id, subscriber_id):

    """This method authorises the Teacher and then unsubscribes  the selected student."""

    check_if_student_or_guest(Teacher)

    if Teacher.get('role').lower() == 'teacher' and check_owner(Teacher, course_id) is None:
        raise Unauthorized

    data.database.update_query('DELETE FROM subscription WHERE course_id = %s AND user_id = %s',
                 (course_id, subscriber_id))
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


async def approve_request(user, person_id):
    """This method approves student and teacher registration requests."""

    check_if_student_or_guest(user)
    data.database.update_query('UPDATE users SET status = %s WHERE user_id = %s', ('approved', person_id,))
    return 'Request Approved'


async def decline_request(user, person_id):
    """This method declines student and teacher registration requests."""

    check_if_student_or_guest(user)

    data.database.update_query('DELETE FROM users WHERE status = %s AND user_id = %s', ('awaiting', person_id,))

    return 'Request declined, try again after 12 months'


def check_if_student_or_guest(user):
    """This method authorises the user and raises error if it's not successful."""

    if user is None or user.get('role').lower() == 'student':
        raise Unauthorized


def check_if_student(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role').lower() == 'student':
        raise Unauthorized


def check_if_guest(user):
    """This method authorises the user and raises error if it's not successful."""

    if user is None:
        raise Unauthorized


def check_if_admin_or_owner(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role').lower() != 'admin' or user.get('role').lower() != 'owner':
        raise Unauthorized


