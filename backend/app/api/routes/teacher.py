from typing import Annotated

from fastapi import APIRouter, Depends
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.teacher_services import get_information, update_information, course_subscribers, \
    view_student_requests

from backend.app.api.utils.utilities import unsubscribe, approve_student, decline_student
from backend.app.models import UpdateProfile


teacher_router = APIRouter(prefix='/teacher_panel')
user_dependency = Annotated[dict, Depends(get_current_user)]


@teacher_router.get('/', status_code=200)
async def account_information(user: user_dependency):
    """
    This method returns the profile information of the user.
    """
    return await get_information(user)


@teacher_router.patch('/personal_information', status_code=200)
async def update_personal_information(user: user_dependency, update: UpdateProfile):
    """
    This method updates selectively the personal information of the user.
    """
    return await update_information(user, update)


@teacher_router.get('/{course_id}/subscribers', status_code=200)
async def view_subscribers(user: user_dependency, course_id: int):
    """
    This method returns a list with all active subscribers of a specific course.
    """
    return await course_subscribers(user, course_id)

@teacher_router.delete('/{course_id}/subscriber/{subscriber_id}', status_code=200)
async def remove_subscriber(user: user_dependency, course_id: int, subscriber_id: int):
    """
    This method removes a subscriber from a specific course.
    """
    return await unsubscribe(user,course_id, subscriber_id)

@teacher_router.get('/pending_requests', status_code=200)
async def view_pending_requests_from_students(user: user_dependency):
    """
    This method views all pending registrations from students.
    """
    return await view_student_requests(user)


@teacher_router.patch('/registration_request', status_code=200)
async def approve_student_request(user: user_dependency, student_id: int):
    """
    This method approves one by one each registration request.
    """
    return await approve_student(user, student_id)


@teacher_router.delete('/registration_request', status_code=200)
async def decline_student_request(user: user_dependency, student_id: int):
    """
    This method declines one by one each registration request.
    """
    return await decline_student(user, student_id)
