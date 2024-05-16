from backend.app.api.routes.section import *
import pytest


@pytest.mark.asyncio
async def test_create_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await create_section(None, None)

    assert isinstance(exc_info.value, Unauthorized)



@pytest.mark.asyncio
async def test_all_sections_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await all_sections(None)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await specific_section(None, None)

    assert isinstance(exc_info.value, Unauthorized)


@pytest.mark.asyncio
async def test_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await delete_section(None, None)

    assert isinstance(exc_info.value, Unauthorized)

