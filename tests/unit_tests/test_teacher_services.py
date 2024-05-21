import pytest

from backend.app.api.services.teacher_services import get_information, update_information, course_subscribers
from backend.app.api.utils.responses import Unauthorized, NotFound
from backend.app.api.utils.utilities import format_personal_information, format_subscription_details
from tests.unit_tests.mock_data import MOCK_USER_DETAILS, MOCK_UPDATE_INFORMATION, teacher_mock, \
    MOCK_SUBSCRIPTION_DETAILS


@pytest.mark.asyncio
async def test_get_information_when_unauthorized():
    with pytest.raises(Unauthorized) as exc_info:
        await get_information(None)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_get_information_when_authorized():
    user = MOCK_USER_DETAILS
    expected = format_personal_information(MOCK_USER_DETAILS)
    result  = await get_information(user)

    assert result == expected


@pytest.mark.asyncio
async def test_update_information_when_unauthorized():
    with pytest.raises(Unauthorized) as exc_info:
        await update_information(None, 'update')

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_update_information_when_authorized(mocker):
    user = MOCK_USER_DETAILS
    update = MOCK_UPDATE_INFORMATION
    mocker.patch('backend.app.api.services.teacher_services.data', mocker.MagicMock())
    result = await update_information(user,update)

    assert result == 'Profile Update successfully'

@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_but_not_as_teacher():
    with pytest.raises(Unauthorized) as exc_info:
        await course_subscribers(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_as_teacher_but_not_the_owner(mocker):
    teacher = teacher_mock()
    with pytest.raises(Unauthorized) as exc_info:
        mocker.patch('backend.app.api.services.teacher_services.check_owner', mocker.MagicMock(return_value = None))
        await course_subscribers(teacher, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_as_teacher_and_the_owner_but_the_return_list_is_empty(mocker):
    teacher = teacher_mock()
    with pytest.raises(NotFound) as exc_info:
        mocker.patch('backend.app.api.services.teacher_services.check_owner',
                     mocker.MagicMock(return_value='Prosto go pusni da mine'))

        mocker.patch('backend.app.api.services.teacher_services.data',
                     mocker.MagicMock(return_value=None))
        await course_subscribers(teacher, 1)


    assert isinstance(exc_info.value, NotFound)

@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_as_teacher_and_the_owner_and_the_return_list_is__not_empty(mocker):
    teacher = teacher_mock()
    expected = format_subscription_details(MOCK_SUBSCRIPTION_DETAILS)

    mocker.patch('backend.app.api.services.teacher_services.check_owner',
                 mocker.MagicMock(return_value='Prosto go pusni da mine'))
    mocker.patch('backend.app.api.services.teacher_services.data',
                 mocker.MagicMock(return_value=MOCK_SUBSCRIPTION_DETAILS))
    result = await course_subscribers(teacher, 1)

    assert result == expected