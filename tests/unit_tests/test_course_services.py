import pytest
from fastapi import HTTPException

from backend.app.api.services.course_services import new_course, delete_course, view_all, view_particular, \
    switch_status, subscribe, rate
from backend.app.api.services.uploadpic_services import check_for_creator
from backend.app.api.services.section_services import sections
from backend.app.api.utils.utilities import format_ratings, format_course_info, get_course_sections
from backend.app.models import Course
from backend.app import data


@pytest.mark.asyncio
async def test_new_course_as_student():
    with pytest.raises(HTTPException) as exc_info:
        await new_course(1, 'student', Course(title="Test Course", description="Test Description", objectives="Test Objectives", owner="Test Owner", status="public", tags=["tag1", "tag2"]))
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "As a student, you cannot create courses!"


@pytest.mark.asyncio
async def test_new_course_not_approved_user(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_if_user_is_approved', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        await new_course(1, 'teacher', Course(title="Test Course", description="Test Description", objectives="Test Objectives", owner="Test Owner", status="public", tags=["tag1", "tag2"]))
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "In order to create a course, you must be approved first!"


@pytest.mark.asyncio
async def test_new_course_existing_course(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_if_user_is_approved', return_value=True)
    mocker.patch('backend.app.api.services.admin_services.check_for_existing_course', return_value=True)
    with pytest.raises(HTTPException) as exc_info:
        await new_course(1, 'teacher', Course(title="Test Course", description="Test Description", objectives="Test Objectives", owner="Test Owner", status="public", tags=["tag1", "tag2"]))
    assert exc_info.value.status_code == 409
    assert exc_info.value.detail == "A course with this title already exists!"


@pytest.mark.asyncio
async def test_delete_course_as_student():
    with pytest.raises(HTTPException) as exc_info:
        await delete_course(1, 'student', 1)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "As a student you cannot delete courses!"


@pytest.mark.asyncio
async def test_delete_course_as_creator_or_admin(mocker):
    mocker.patch('backend.app.api.services.uploadpic_services.check_for_creator', return_value=True)
    mocker.patch('backend.app.api.services.admin_services.data')
    result = await delete_course(1, 'teacher', 1)
    assert isinstance(result, dict)
    assert result["message"] == "Course deleted!"


@pytest.mark.asyncio
async def test_delete_course_not_creator(mocker):
    mocker.patch('backend.app.api.services.uploadpic_services.check_for_creator', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        await delete_course(1, 'teacher', 1)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You are not the creator of this course!"


@pytest.mark.asyncio
async def test_view_all_courses(mocker):
    mocker.patch('backend.app.api.services.admin_services.data')
    mocker.patch('backend.app.api.utils.utilities.format_course_info', return_value=[{"title": "Test Course"}])
    result = view_all(None, 1, 10)
    assert isinstance(result, dict)
    assert "Courses" in result


@pytest.mark.asyncio
async def test_view_particular_course_not_approved(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_if_user_is_approved', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        await view_particular(1, 1, 'student')
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You must be approved in order to view courses!"


@pytest.mark.asyncio
async def test_view_particular_premium_course_not_subscribed(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_if_user_is_approved', return_value=True)
    mocker.patch('backend.app.api.services.admin_services.check_course_status', return_value="premium")
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        await view_particular(1, 1, 'student')
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You must be subscribed in order to see this course!"


@pytest.mark.asyncio
async def test_switch_status_as_student():
    with pytest.raises(HTTPException) as exc_info:
        switch_status(1, 'student', 1)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "As a student you cannot switch course status!"


@pytest.mark.asyncio
async def test_switch_status_as_teacher_or_admin(mocker):
    mocker.patch('backend.app.api.services.uploadpic_services.check_for_creator', return_value=True)
    mocker.patch('backend.app.api.services.admin_services.data')
    mocker.patch('backend.app.api.services.admin_services.check_course_status', return_value="public")
    result = switch_status(1, 'teacher', 1)
    assert isinstance(result, dict)
    assert result["message"] == "Course status switched to Premium"


@pytest.mark.asyncio
async def test_subscribe_already_subscribed(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=True)
    with pytest.raises(HTTPException) as exc_info:
        subscribe(1, 1)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You already subscribed to this course!"


@pytest.mark.asyncio
async def test_subscribe_not_approved(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=False)
    mocker.patch('backend.app.api.services.admin_services.check_if_user_is_approved', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        subscribe(1, 1)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You must be approved in order to subscribe to courses"


@pytest.mark.asyncio
async def test_rate_not_subscribed(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=False)
    with pytest.raises(HTTPException) as exc_info:
        rate(1, 1, 5)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You cannot rate courses you aren't subscribed to!"


@pytest.mark.asyncio
async def test_rate_own_course(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=True)
    mocker.patch('backend.app.api.services.uploadpic_services.check_for_creator', return_value=True)
    with pytest.raises(HTTPException) as exc_info:
        rate(1, 1, 5)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You cannot rate your own courses!"


@pytest.mark.asyncio
async def test_rate_already_rated(mocker):
    mocker.patch('backend.app.api.services.admin_services.check_for_subscription', return_value=True)
    mocker.patch('backend.app.api.services.uploadpic_services.check_for_creator', return_value=False)
    mocker.patch('backend.app.api.services.admin_services.check_for_rating', return_value=True)
    with pytest.raises(HTTPException) as exc_info:
        rate(1, 1, 5)
    assert exc_info.value.status_code == 403
    assert exc_info.value.detail == "You have already rated this course!"
