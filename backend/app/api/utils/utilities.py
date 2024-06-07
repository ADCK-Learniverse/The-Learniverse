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
    return {'Course Subscribers': formatted_details}


def format_section_details(section_details_list):
    """This method formats the section information list."""
    sections = [{
            'Section Title': format_detail[1],
            'Section Content': format_detail[2],
            'Section Description': format_detail[3],
            'Section Information': format_detail[4],
            'Course ID': format_detail[5],
        } for format_detail in section_details_list]
    return sections


def check_owner(Teacher, course_id):
    """This method checks if the Teacher is the owner of the course."""

    Teacher_name = f"{Teacher.get('first_name')} {Teacher.get('last_name')}"

    info = data.database.read_query('SELECT * FROM courses WHERE course_id = %s AND owner = %s',
                      (course_id, Teacher_name))
    if info:
        return info



async def unsubscribe(Teacher, course_id, subscriber_id):

    """This method authorises the Teacher and then unsubscribes  the selected student."""

    check_if_guest(Teacher)
    check_if_student(Teacher)

    if Teacher.get('role').lower() == 'teacher' and check_owner(Teacher, course_id) is None:
        raise Unauthorized

    data.database.update_query('DELETE FROM subscription WHERE course_id = %s AND user_id = %s',
                 (course_id, subscriber_id))
    return {"message": "User unsubscribed successfully"}


def format_course_info(content: list):
    return [
        {
            "Course ID": course[0],
            "Course Title": course[1],
            "Description": course[2],
            "Rating": course[3],
            "Status": course[4],
            "By": course[5],
            "Tags": course[6]
        }
        for course in content
    ]


def format_ratings(content: list):
    return [
        {
            "User": get_user_names(rating[0]),
            "Rating": rating[1]
        }
        for rating in content
    ]


def format_user_info(content: list):
    return [
        {
            "First name": user[0],
            "Last name": user[1],
            "Email": user[2],
            "Phone number": user[3] if user[3] else "Not provided",
            "Role": user[4],
            "Status": user[5]
        }
        for user in content
    ]


def get_user_names(user_id: int):
    sql = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    execute = data.database.read_query(sql, (user_id,))
    names = execute[0][0] + " " + execute[0][1]
    return names


async def approve_student(user, person_id):
    """This method approves student registration requests."""

    check_if_guest(user)
    check_if_student(user)

    data.database.update_query('UPDATE users SET status = %s WHERE user_id = %s', ('approved', person_id,))
    return {"message": "Request Approved!"}


async def approve_teacher(user, person_id):
    """This method approves teacher and teacher registration requests."""

    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)


    data.database.update_query('UPDATE users SET status = %s WHERE user_id = %s', ('approved', person_id,))
    return {"message": "Request Approved!"}


def get_course_sections(course_id: int):
    sql = "SELECT title, content, description, information, section_id FROM sections WHERE course_id = %s"
    execute = data.database.read_query(sql, (course_id,))
    if execute:
        formatted = [
            {
                "Title": row[0],
                "Content": row[1],
                "Description": row[2],
                "Information": row[3],
                "Section ID": row[4]
            }
            for row in execute
        ]
        return formatted
    return execute


def mark_section_as_visited(user_id: int, section_id: int):
    sql = "SELECT visited_sections FROM users WHERE user_id = %s"
    student_data = data.database.read_query(sql, (user_id,))

    if not student_data:
        visited_sections_str = ''
    else:
        visited_sections_str = student_data[0][0]

    visited_sections = set(map(int, visited_sections_str.split(','))) if visited_sections_str else set()
    visited_sections.add(section_id)
    updated_visited_sections_str = ','.join(map(str, visited_sections))

    update_sql = "UPDATE users SET visited_sections = %s WHERE user_id = %s"
    data.database.update_query(update_sql, (updated_visited_sections_str, user_id))


async def decline_student(user, person_id):
    """This method declines student and teacher registration requests."""

    check_if_guest(user)
    check_if_student(user)

    data.database.update_query('DELETE FROM users WHERE status = %s AND user_id = %s', ('awaiting', person_id,))

    return {"message": "Request declined, try again after 12 months!"}


async def decline_teacher(user, person_id):
    """This method declines student and teacher registration requests."""

    check_if_guest(user)
    check_if_student(user)
    check_if_teacher(user)

    data.database.update_query('DELETE FROM users WHERE status = %s AND user_id = %s', ('awaiting', person_id,))

    return {"message": "Request declined, try again after 12 months!"}


def check_if_guest(user):
    """This method authorises the user and raises error if it's not successful."""

    if user is None:
        raise Unauthorized


def check_if_student(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role').lower() == 'student':
        raise Unauthorized


def check_if_admin(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role')== 'admin':
        raise Unauthorized


def check_if_owner(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role') == 'owner':
        raise Unauthorized
def check_if_teacher(user):
    """This method authorises the user and raises error if it's not successful."""

    if user.get('role') == 'teacher':
        raise Unauthorized

def check_for_creator(user_id, course_id):
    course_names_sql = "SELECT owner FROM courses WHERE course_id = %s"
    execute_course = data.database.read_query(course_names_sql, (course_id,))
    course_owner = execute_course[0][0]
    names_sql = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    execute = data.database.read_query(names_sql, (user_id,))
    names = execute[0][0] + " " + execute[0][1]
    if names == course_owner:
        return True
    return False


def paginate_query(base_sql, page=1, size=10):
    start = (page - 1) * size
    paginated_sql = f"{base_sql} LIMIT {size} OFFSET {start}"

    return paginated_sql

def format_requests(requests_details_list):
    """This method formats the section information list."""
    requests = [{
            'User ID': request_detail[0],
            'Email': request_detail[1],
            'First Name': request_detail[2],
            'Last Name': request_detail[3],
            'Phone Number': request_detail[4],
        } for request_detail in requests_details_list ]
    return requests

