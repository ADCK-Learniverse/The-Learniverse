from backend.app.api.routes.section import *
import pytest

from backend.app.api.utils.responses import Unauthorized


@pytest.mark.asyncio
async def test_create_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await create_section(None, None)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_all_sections_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await all_sections(None, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_specific_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await specific_section(None, None, 1)

    assert isinstance(exc_info.value, Unauthorized)

@pytest.mark.asyncio
async def test_delete_section_when_guest():
    with pytest.raises(Unauthorized) as exc_info:
        await delete_section(None, None, None)

    assert isinstance(exc_info.value, Unauthorized)

