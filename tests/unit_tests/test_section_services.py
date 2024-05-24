import pytest
from backend.app.api.services.section_services import sections, section, remove_section
from backend.app.api.utils.responses import Unauthorized
from backend.app.api.utils.utilities import format_section_details

from tests.unit_tests.mock_data import teacher_mock, MOCK_SECTION_DETAILS


@pytest.mark.asyncio
async def test_sections_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services', mocker.MagicMock(return_value=None))
    with pytest.raises(Unauthorized) as exc_info:
       await sections(None, 1)

    assert isinstance(exc_info.value, Unauthorized)
#

# @pytest.mark.asyncio
# async def test_section_when_any(mocker):
#     data = MOCK_SECTION_DETAILS
#     teacher = teacher_mock()
#     expected = format_section_details(MOCK_SECTION_DETAILS)
#     mocker.patch('backend.app.api.services.section_services.data', mocker.MagicMock(return_value = data))
#     result = await section(teacher,1,1)
#     assert result == expected
#

@pytest.mark.asyncio
async def test_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services', mocker.MagicMock(return_value=None))
    with pytest.raises(Unauthorized) as exc_info:
        await section(None, 1,1,)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_remove_section_when_it_exist(mocker):
    teacher = teacher_mock()
    mocker.patch('backend.app.api.services.section_services.check_for_creator', mocker.MagicMock(return_value = 'Any'))
    mocker.patch('backend.app.api.services.section_services.data', mocker.MagicMock(return_value='Any'))
    mocker.patch('backend.app.api.services.section_services.data')
    result = await remove_section(teacher, 1, 1)

    assert result == {"message": "Section Deleted!"}


@pytest.mark.asyncio
async def test_remove_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.data', mocker.MagicMock(return_value=None))
    mocker.patch('backend.app.api.services.section_services.data')
    with pytest.raises(Unauthorized) as exc_info:
        await remove_section(None, 1, 1)

    assert isinstance(exc_info.value, Unauthorized)


