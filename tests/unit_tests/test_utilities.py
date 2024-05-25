# Test Decline_teacher
# test decline_student
# test approve teacher
# test approve student
# test unsubscribe
import pytest

from backend.app.api.utils.responses import Unauthorized
from backend.app.api.utils.utilities import approve_student, approve_teacher, decline_student, decline_teacher, \
    unsubscribe


@pytest.mark.asyncio
async def test_approve_student_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await  approve_student(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_approve_student_as_student():
    with pytest.raises(Unauthorized) as exc_info:
        await  approve_student({'role': 'student'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_approve_student_as_teacher(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')

    result = await approve_student({'role': 'teacher'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_approve_student_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await approve_student({'role': 'teacher or admin or owner'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_approve_teacher_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await  approve_teacher(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_approve_teacher_as_student():
    with pytest.raises(Unauthorized) as exc_info:
        await  approve_teacher({'role': 'student'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_approve_teacher_as_teacher():
    with pytest.raises(Unauthorized) as exc_info:
        await  approve_teacher({'role': 'teacher'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_approve_teacher_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await approve_student({'role': 'teacher'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_decline_student_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await  decline_student(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_decline_student_as_student():
    with pytest.raises(Unauthorized) as exc_info:
        await  decline_student({'role': 'student'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_decline_student_as_teacher(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')

    result = await decline_student({'role': 'teacher'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_decline_student_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await decline_student({'role': 'teacher or admin or owner'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_decline_teacher_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await  decline_teacher(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_decline_teacher_as_student():
    with pytest.raises(Unauthorized) as exc_info:
        await  decline_teacher({'role': 'student'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_decline_teacher_as_teacher():
    with pytest.raises(Unauthorized) as exc_info:
        await  decline_teacher({'role': 'teacher'}, 1)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_decline_teacher_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await decline_teacher({'role': 'admin or owner'}, 1)

    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_unsubscribe_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await  unsubscribe(None, 1, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_remove_subscriber_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await unsubscribe(None, 1, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_unsubscribe_as_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await unsubscribe(None, 1, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_unsubscribe_as_teacher_but_not_owner_of_course(mocker):
    mocker.patch('backend.app.api.utils.utilities.check_owner', mocker.MagicMock(return_value = None))
    with pytest.raises(Unauthorized) as exc_info:
        await unsubscribe(None, 1, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_unsubscribe_as_teacher_and_owner_of_course(mocker):
    mocker.patch('backend.app.api.utils.utilities.check_owner', mocker.MagicMock(return_value = 'Any'))
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await unsubscribe({'role':'teacher'}, 1, 1)

    assert isinstance(result, dict)

@pytest.mark.asyncio
async def test_unsubscribe_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.utils.utilities.check_owner', mocker.MagicMock(return_value = 'Any'))
    mocker.patch('backend.app.api.utils.utilities.data')
    result = await unsubscribe({'role':'teacher or admin or owner'}, 1, 1)

    assert isinstance(result, dict)




