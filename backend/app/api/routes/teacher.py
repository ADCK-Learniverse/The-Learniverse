from typing import Annotated
from fastapi import APIRouter, Depends
from backend.app.api.routes.profile import profile_related_endpoints
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.teacher_services import course_subscribers, view_student_requests
from backend.app.api.utils.utilities import unsubscribe, approve_student, decline_student

teacher_router = APIRouter(prefix='/teacher_panel')
user_dependency = Annotated[dict, Depends(get_current_user)]
profile_related_endpoints(teacher_router)


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
    return await unsubscribe(user, course_id, subscriber_id)


@teacher_router.get('/student/pending_requests', status_code=200)
async def view_pending_requests_from_students(user: user_dependency):
    """
    This method views all pending registrations from students.
    """
    return await view_student_requests(user)


@teacher_router.patch('/student/registration_request', status_code=200)
async def approve_student_request(user: user_dependency, student_id: int):
    """
    This method approves one by one each registration request from students.
    """
    return await approve_student(user, student_id)


@teacher_router.delete('/student/registration_request', status_code=200)
async def decline_student_request(user: user_dependency, student_id: int):
    """
    This method declines one by one each registration request from students.
    """
    return await decline_student(user, student_id)


def teacher_related_endpoints(router: APIRouter):
    router.get('/{course_id}/subscribers', status_code=200)(view_subscribers)
    router.get('/student/pending_requests', status_code=200)(view_pending_requests_from_students)
    router.delete('/{course_id}/subscriber/{subscriber_id}', status_code=200)(remove_subscriber)
    router.delete('/registration_request', status_code=200)(decline_student_request)
    router.patch('/registration_request', status_code=200)(approve_student_request)
