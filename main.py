import uvicorn
from fastapi import FastAPI
from backend.app.api.routes.login import login_router, logout_router
from backend.app.api.routes.register import register_router
from backend.app.api.routes.uploadpic import picture_router
from backend.app.api.routes.course import course_router


app = FastAPI()

LOGIN_REGISTER = "Login / Register"


@app.get('/')
def home():
    return {"message": "Hello!"}


app.include_router(login_router, tags=[LOGIN_REGISTER])
app.include_router(logout_router, tags=[LOGIN_REGISTER])
app.include_router(register_router, tags=[LOGIN_REGISTER])
app.include_router(picture_router, tags=["Profile / Course Pictures"])
app.include_router(course_router, tags=["Courses"])


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)