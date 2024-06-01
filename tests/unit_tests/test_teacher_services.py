import pytest

from backend.app.api.services.teacher_services import  course_subscribers, \
    view_student_requests
from backend.app.api.utils.responses import Unauthorized, NotFound
from backend.app.api.utils.utilities import format_personal_information, format_subscription_details
from tests.unit_tests.mock_data import MOCK_USER_DETAILS, MOCK_UPDATE_INFORMATION, teacher_mock, \
    MOCK_SUBSCRIPTION_DETAILS


@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_but_not_as_teacher():
    # Arrange & Act
    with pytest.raises(Unauthorized) as exc_info:
        await course_subscribers(None, 1)
    # Assert
    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_course_subscribers_when_authorized_as_teacher_but_not_the_owner(mocker):
    # Arrange & Act
    teacher = teacher_mock()
    with pytest.raises(Unauthorized) as exc_info:
        mocker.patch('backend.app.api.services.teacher_services.check_owner', mocker.MagicMock(return_value = None))
        await course_subscribers(teacher, 1)
    # Assert
    assert isinstance(exc_info.value, Unauthorized)

# @pytest.mark.asyncio
# async def test_course_subscribers_when_authorized_as_teacher_and_the_owner_but_the_return_list_is_empty(mocker):
#     teacher = teacher_mock()
#     with pytest.raises(NotFound) as exc_info:
#         mocker.patch('backend.app.api.services.teacher_services.check_owner',
#                      mocker.MagicMock(return_value='Prosto go pusni da mine'))
#
#         mocker.patch('backend.app.api.services.teacher_services.data',
#                      mocker.MagicMock(return_value=None))
#         await course_subscribers(teacher, 1)
#
#
#     assert isinstance(exc_info.value, NotFound)
#
# @pytest.mark.asyncio
# async def test_course_subscribers_when_authorized_as_teacher_and_the_owner_and_the_return_list_is__not_empty(mocker):
#     teacher = teacher_mock()
#     expected = format_subscription_details(MOCK_SUBSCRIPTION_DETAILS)
#
#     mocker.patch('backend.app.api.services.teacher_services.check_owner',
#                  mocker.MagicMock(return_value='Prosto go pusni da mine'))
#     mocker.patch('backend.app.api.services.teacher_services.data',
#                  mocker.MagicMock(return_value=MOCK_SUBSCRIPTION_DETAILS))
#     result = await course_subscribers(teacher, 1)
#
#     assert result == expected

@pytest.mark.asyncio
async def test_view_student_requests_when_authenticated_as_student_or_guest():
    # Arrange & Act
    with pytest.raises(Unauthorized) as exc_info:
        await view_student_requests(None)
    # Assert
    assert isinstance(exc_info.value, Unauthorized)

# @pytest.mark.asyncio
# async def test_view_student_requests_when_authenticated_as_teacher_but_list_is_empty(mocker):
#     teacher = teacher_mock()
#
#     mocker.patch('backend.app.api.services.teacher_services.data',return_value=None)
#     result = await view_student_requests(teacher)
#
#     assert result == 'No pending requests'
