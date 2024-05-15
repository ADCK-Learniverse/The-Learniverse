import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.app.api.routes.login import login_router, logout_router
from backend.app.api.routes.register import register_router
from backend.app.api.routes.uploadpic import picture_router
from backend.app.api.routes.course import course_router
# from routers.topics import topics_router
# from routers.admin import admin_router
# from routers.messenger import messenger_router
# from routers.users import users_router
# from routers.reply import reply_router


app = FastAPI()

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


app.include_router(login_router, tags=["Login / Register"])
app.include_router(logout_router, tags=["Login / Register"])
app.include_router(register_router, tags=["Login / Register"])
app.include_router(picture_router, tags=["Profile / Course Pictures"])
app.include_router(course_router, tags=["Courses"])
# app.include_router(categories_router, tags=["Category"])
# app.include_router(topics_router, tags=["Topics"])
# app.include_router(users_router, tags=["Admin"])
# app.include_router(messenger_router, tags=["Messenger"])
# app.include_router(admin_router, tags=["Admin"])
# app.include_router(owner_router, tags=["Owner"])
# app.include_router(reply_router, tags=['Topic Replies'])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)