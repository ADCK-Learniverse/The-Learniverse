import uvicorn
from fastapi import FastAPI, Request
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
from backend.app.api.services.login_services import get_current_user

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


@app.middleware("http")
async def add_token_refresh_header(request: Request, call_next):
    excluded_paths = ["/login", "/register", "/logout"]
    if not any(request.url.path.startswith(path) for path in excluded_paths):
        response = await call_next(request)
        print("Request URL:", request.url)
        print("Request Headers:", request.headers)
        print("Response:", response)
        if "Authorization" in request.headers:
            token = request.headers.get("Authorization").split(" ")[1]
            try:
                user = get_current_user(token)
                new_token = user.get("new_token")
                if new_token:
                    response.headers['Authorization'] = f'Bearer {new_token}'
            except Exception as e:
                print(f"Error in token refresh: {e}")
        return response
    else:
        return await call_next(request)

@app.get('/')
def home():
    return {"message": "Hello!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)