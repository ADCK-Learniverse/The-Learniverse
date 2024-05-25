import pytest

from backend.app.api.services.admin_services import deactivate, view_teacher_requests
from backend.app.api.utils.responses import Unauthorized


@pytest.mark.asyncio
async def test_deactivate_account_as_guest():
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate(None, 1)

        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_deactivate_account_as_student():
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate({'role':'student'}, 1)

        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_deactivate_account_as_teacher():
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate({'role':'teacher'}, 1)

        assert isinstance(exc_info.value, Unauthorized)
@pytest.mark.asyncio
async def test_deactivate_account_as_admin_or_owner(mocker):
    mocker.patch('backend.app.api.services.admin_services.data')
    result = await deactivate({'role':'admin or owner'}, 1)

    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_view_teacher_requests_as_guest():
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests(None)

        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_view_teacher_requests_as_student():
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests({'role':'student'})

        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_view_teacher_requests_as_teacher():
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests({'role':'teacher'})

        assert isinstance(exc_info.value, Unauthorized)

