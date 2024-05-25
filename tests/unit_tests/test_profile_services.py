import pytest

from backend.app.api.services.profile_services import update_phone, update_lastname, update_firstname, update_password


@pytest.mark.asyncio
async def test_update_phone(mocker):
    mocker.patch('backend.app.api.services.profile_services.data')
    result =  update_phone(1, "8888888888")

    assert result  == {"message": "Phone number updated!"}

@pytest.mark.asyncio
async def test_update_firstname(mocker):
    mocker.patch('backend.app.api.services.profile_services.data')
    result = update_firstname(1, '8798746546')

    assert result == {"message": "First name updated!"}

@pytest.mark.asyncio
async def test_update_lastname(mocker):
    mocker.patch('backend.app.api.services.profile_services.data')
    result = update_lastname(1, '8798746546')

    assert result == {"message": "Last name updated!"}

@pytest.mark.asyncio
async def test_update_password(mocker):
    mocker.patch('backend.app.api.services.profile_services.data')
    result = update_password({'id':1}, '8798746546')

    assert result == {"message": "Password updated!"}


