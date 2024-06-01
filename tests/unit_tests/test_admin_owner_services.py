import pytest

from backend.app.api.services.admin_services import deactivate, view_teacher_requests
from backend.app.api.utils.responses import Unauthorized


@pytest.mark.asyncio
async def test_deactivate_account_as_guest():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate(None, 1)
    # Assert
        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_deactivate_account_as_student():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate({'role':'student'}, 1)
    # Assert
        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_deactivate_account_as_teacher():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await deactivate({'role':'teacher'}, 1)
    # Assert
        assert isinstance(exc_info.value, Unauthorized)
@pytest.mark.asyncio
async def test_deactivate_account_as_admin_or_owner(mocker):
    # Arrange and Act
    mocker.patch('backend.app.api.services.admin_services.data')
    result = await deactivate({'role':'admin or owner'}, 1)
    # Assert
    assert isinstance(result, dict)


@pytest.mark.asyncio
async def test_view_teacher_requests_as_guest():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests(None)
    # Assert
        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_view_teacher_requests_as_student():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests({'role':'student'})
    # Assert
        assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_view_teacher_requests_as_teacher():
    # Arrange and Act
        with pytest.raises(Unauthorized) as exc_info:
            await view_teacher_requests({'role':'teacher'})
    # Assert
        assert isinstance(exc_info.value, Unauthorized)

