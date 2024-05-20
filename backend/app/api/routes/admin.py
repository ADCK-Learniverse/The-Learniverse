from typing import Annotated

from fastapi import APIRouter, Depends

from backend.app.api.services.login_services import get_current_user
from backend.app.api.utils.responses import Unauthorized
from backend.app.api.utils.utilities import unsubscribe

admin_router = APIRouter(prefix="/admin_panel")
user_dependency = Annotated[dict, Depends(get_current_user)]


@admin_router.delete('/{course_id}/subscriber/{subscriber_id}', status_code=200)
async def remove_subscriber(user: user_dependency, course_id, subscriber_id):
    if user is None or user.get('role').lower() == 'student':
        raise Unauthorized

    return await unsubscribe(user,course_id, subscriber_id)
