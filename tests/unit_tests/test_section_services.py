import pytest
from backend.app.api.services.section_services import format_section_details, sections, section, remove_section
from backend.app.api.utils.responses import NoContent, NotFound
from tests.unit_tests.mock_data import MOCK_SECTION_DETAILS



def test_something():
    assert 10 == 10

# @pytest.mark.asyncio
# async def test_sections_when_any(mocker):
#     data = MOCK_SECTION_DETAILS
#     expected = format_section_details(MOCK_SECTION_DETAILS)
#     mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value = data))
#     # Mocking the database connector (mydb)
#     mydb_mock = mocker.Mock()
#     mydb_mock.side_effect = Exception("Database connection error")
#     mocker.patch('backend.app.data.database.mydb', mydb_mock)
#
#     result = await sections()
#     assert result == expected


@pytest.mark.asyncio
async def test_sections_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    with pytest.raises(NoContent) as exc_info:
        await sections()

    assert isinstance(exc_info.value, NoContent)
#

@pytest.mark.asyncio
async def test_section_when_any(mocker):
    data = MOCK_SECTION_DETAILS
    expected = format_section_details(MOCK_SECTION_DETAILS)
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value = data))
    result = await section(1)
    assert result == expected


@pytest.mark.asyncio
async def test_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    with pytest.raises(NoContent) as exc_info:
        await section(1)

    assert isinstance(exc_info.value, NoContent)


@pytest.mark.asyncio
async def test_remove_section_when_it_exist(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value='Any'))
    mocker.patch('backend.app.api.services.section_services.update_query')
    result = await remove_section(1)

    assert result == "Section deleted"


@pytest.mark.asyncio
async def test_remove_section_when_None(mocker):
    mocker.patch('backend.app.api.services.section_services.read_query', mocker.MagicMock(return_value=None))
    mocker.patch('backend.app.api.services.section_services.update_query')
    with pytest.raises(NotFound) as exc_info:
        await remove_section(1)

    assert isinstance(exc_info.value, NotFound)


