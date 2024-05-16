import os

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


MOCK_SECTION_DETAILS = [(1, 'Title', "Content", "Description", "Information", "Course name")]