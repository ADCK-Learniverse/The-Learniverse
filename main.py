import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.api.routes.admin import admin_router
from backend.app.api.routes.login import login_router, logout_router
from backend.app.api.routes.owner import owner_router
from backend.app.api.routes.register import register_router
from backend.app.api.routes.section import section_router
from backend.app.api.routes.student import student_router
from backend.app.api.routes.teacher import teacher_router
from backend.app.api.routes.uploadpic import picture_router
from backend.app.api.routes.course import course_router


app = FastAPI()

LOGIN_REGISTER = "Login / Register"

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get('/')
def home():
    return {"message": "Hello!"}


app.include_router(login_router, tags=[LOGIN_REGISTER])
app.include_router(logout_router, tags=[LOGIN_REGISTER])
app.include_router(register_router, tags=[LOGIN_REGISTER])
app.include_router(picture_router, tags=["Profile / Course Pictures"])
app.include_router(course_router, tags=["Courses"])
app.include_router(section_router, tags=["Sections"])
app.include_router(teacher_router, tags=['Teacher Panel'])
app.include_router(admin_router, tags=['Admin Panel'])
app.include_router(owner_router, tags=['Owner Panel'])
app.include_router(student_router, tags=['Student Panel'])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)