import pytest
from fastapi import HTTPException
from backend.app import data
from backend.app.api.utils.utilities import format_user_info
from backend.app.api.services.course_services import view_particular
from backend.app.api.services.student_services import welcome_message, view_subscriptions


@pytest.mark.asyncio
async def test_welcome_message(mocker):
    mocker.patch('backend.app.data.database.read_query', return_value=[["John"]])
    result = welcome_message(1)
    assert isinstance(result, dict)
    assert result["message"] == "Hello, John"


@pytest.mark.asyncio
async def test_welcome_message_user_not_found(mocker):
    mocker.patch('backend.app.data.database.read_query', return_value=[])
    with pytest.raises(IndexError):
        await welcome_message(1)


@pytest.mark.asyncio
async def test_view_subscriptions_no_subscriptions(mocker):
    mocker.patch('backend.app.data.database.read_query', side_effect=[
        [],
        [[0]]
    ])
    with pytest.raises(HTTPException) as exc_info:
        await view_subscriptions(1, 'student')
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "No subscriptions found!"


@pytest.mark.asyncio
async def test_view_subscriptions_with_subscriptions(mocker):
    mocker.patch('backend.app.data.database.read_query', side_effect=[
        [[1]],
        [[1]]
    ])
    mocker.patch('backend.app.api.services.course_services.view_particular', return_value={"course": "details"})

    result = view_subscriptions(1, 'student')
    assert isinstance(result, dict)
    assert "Courses you're subscribed to: 1" in result
    assert result["Page"] == 1
    assert result["Size"] == 10
    assert result["Courses you're subscribed to: 1"] == [{"course": "details"}]


@pytest.mark.asyncio
async def test_view_subscriptions_multiple_pages(mocker):
    mocker.patch('backend.app.data.database.read_query', side_effect=[
        [[1], [2]],
        [[2]]
    ])
    mocker.patch('backend.app.api.services.course_services.view_particular', return_value={"course": "details"})

    result = await view_subscriptions(1, 'student', page=2, size=1)
    assert isinstance(result, dict)
    assert "Courses you're subscribed to: 2" in result
    assert result["Page"] == 2
    assert result["Size"] == 1
    assert result["Courses you're subscribed to: 2"] == [{"course": "details"}, {"course": "details"}]


@pytest.mark.asyncio
async def test_view_subscriptions_empty_page(mocker):
    mocker.patch('backend.app.data.database.read_query', side_effect=[
        [],
        [[1]]
    ])

    with pytest.raises(HTTPException) as exc_info:
        await view_subscriptions(1, 'student', page=2, size=1)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "No subscriptions found!"
