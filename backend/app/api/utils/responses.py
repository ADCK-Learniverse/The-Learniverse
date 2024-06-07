from fastapi import HTTPException

class BadRequest(HTTPException):
    def __init__(self, content='Bad Request'):
        super().__init__(status_code=400, detail=content)

class NotFound(HTTPException):
    def __init__(self, content='Not Found'):
        super().__init__(status_code=404, detail=content)

class Unauthorized(HTTPException):
    def __init__(self, content='Unauthorized'):
        super().__init__(status_code=401, detail=content)

class NoContent(HTTPException):
    def __init__(self, content='No Content'):
        super().__init__(status_code=204, detail=content)

class InternalServerError(HTTPException):
    def __init__(self, content='Internal Server Error'):
        super().__init__(status_code=500, detail=content)

class AccountNotApproved(HTTPException):
    def __init__(self, content='Your account has no access at this time!'):
        super().__init__(status_code=403, detail=content)