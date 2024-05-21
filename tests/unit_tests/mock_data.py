import os

from backend.app.models import UpdateProfile

NOT_AUTHORIZED = "Not authorized"
NOT_AUTHENTICATED = "Not authenticated"
USER_NOT_FOUND = 'User not found!'
IS_ADMIN = 'Is admin'
secret_key = os.getenv("SECRET_KEY")


def student_mock():
    return {"role": 'student'}

def teacher_mock():
    return {"role": 'teacher'}

def admin_mock():
    return {"role": 'admin'}

def owner_mock():
    return {"role": 'owner'}

MOCK_USER_DETAILS = {'sub': 'username', 'id': 1,
                                     'first_name': 'Alex', 'last_name': 'Daskalov',
                                     'role': 'owner', 'phone_number': '10000000000'}


MOCK_SECTION_DETAILS = [(1, 'Title', "Content", "Description", "Information", "Course name")]

MOCK_UPDATE_INFORMATION = UpdateProfile(First_name='Alex', Last_name='Daskalov',
                                        Phone_number='142545623', Password='string')

MOCK_SUBSCRIPTION_DETAILS = [
    (1, 'Title1', "Content1", "Description1", "Information1", "Course name1"),
    (2, 'Title2', "Content2", "Description2", "Information2", "Course name2"),
    (3, 'Title3', "Content3", "Description3", "Information3", "Course name3"),
]