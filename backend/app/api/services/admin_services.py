from pydantic import Field
from backend.app.data.database import read_query


def get_user_by_id(user_id: int = Field(gt=0)):
    sql = "SELECT * FROM users WHERE user_id = %s"
    result = read_query(sql, (user_id,))
    return result
