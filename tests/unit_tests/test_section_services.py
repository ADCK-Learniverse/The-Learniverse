import pytest
from backend.app.api.services.section_services import sections, section, remove_section
from backend.app.api.utils.responses import NoContent, NotFound, Unauthorized
from backend.app.api.utils.utilities import format_section_details
from tests.unit_tests.mock_data import MOCK_SECTION_DETAILS, teacher_mock


def test_something():
    assert 10 == 10


@pytest.mark.asyncio
async def test_sections_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    with pytest.raises(Unauthorized) as exc_info:
       await sections(None, 1)

    assert isinstance(exc_info.value, Unauthorized)
#

@pytest.mark.asyncio
async def test_section_when_any(mocker):
    data = MOCK_SECTION_DETAILS
    teacher = teacher_mock()
    expected = format_section_details(MOCK_SECTION_DETAILS)
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value = data))
    result = await section(teacher,1,1)
    assert result == expected


@pytest.mark.asyncio
async def test_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    with pytest.raises(Unauthorized) as exc_info:
        await section(None, 1,1,)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_remove_section_when_it_exist(mocker):
    teacher = teacher_mock()
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value='Any'))
    mocker.patch('backend.app.api.services.section_services.update_query')
    result = await remove_section(teacher, 1)

    assert result == "Section deleted"


@pytest.mark.asyncio
async def test_remove_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    mocker.patch('backend.app.api.services.section_services.update_query')
    with pytest.raises(Unauthorized) as exc_info:
        await remove_section(None, 1)

    assert isinstance(exc_info.value, Unauthorized)


