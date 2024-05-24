import pytest

from backend.app.api.routes.profile import update_number


# @pytest.mark.asyncio
# def test_user_profile(mocker):
#     mocker.patch('backend.app.api.routes.profile.update_phone', mocker.MagicMock(return_value = 'Any'))
#     result = update_number({'id':1}, '51216161')
#     assert result.status_code == 201
#
