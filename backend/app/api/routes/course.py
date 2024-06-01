from fastapi import APIRouter, Depends, Query
from backend.app.models import Course
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.course_services import (new_course, switch_status, subscribe,
                                                      delete_course, unsubscribe, rate, view_all,
                                                      view_particular, show_ratings)
from typing import Annotated
import logging

course_router = APIRouter(prefix="/courses")

user_dependency = Annotated[dict, Depends(get_current_user)]



@course_router.get("/all", status_code=200)
def view_all_courses(
    search: str = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    return view_all(search, page, size)


@course_router.get("/{course_id}", status_code=200)
def view_course(user: user_dependency, course_id: int):
    user_id = user.get("id")
    user_role = user.get("role")
    return view_particular(course_id, user_id, user_role)


@course_router.post("/new", status_code=201)
def create_course(user: user_dependency, course: Course):
    logging.debug(user)
    user_id = user.get("id")
    user_role = user.get("role")
    return new_course(user_id, user_role, course)


@course_router.put("/status/{course_id}", status_code=200)
def switch_course_status(user: user_dependency, course_id: int):
    user_role = user.get("role")
    user_id = user.get("id")
    return switch_status(course_id, user_role, user_id)


@course_router.post("/subscription/{course_id}", status_code=201)
def subscribe_to_course(user: user_dependency, course_id: int):
    user_id = user.get("id")
    return subscribe(user_id, course_id)


@course_router.delete("/subscription/{course_id}", status_code=200)
def remove_subscription(user: user_dependency, course_id: int):
    user_id = user.get("id")
    return unsubscribe(user_id, course_id)


@course_router.delete("/", status_code=204)
def course_delete(user: user_dependency, course_id: int):
    user_id = user.get("id")
    user_role = user.get("role")
    return delete_course(user_id, user_role, course_id)


@course_router.post("/rating/{course_id}", status_code=201)
def rate_course(user: user_dependency, course_id: int, rating: int):
    user_id = user.get("id")
    return rate(user_id, course_id, rating)


@course_router.get("/ratings/{course_id}", status_code=200)
def view_ratings(user: user_dependency, course_id: int, page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)):
    return show_ratings(course_id)


def course_related_endpoints(router: APIRouter):
    router.get("/all", status_code=200)(view_all_courses)
    router.get("/{course_id}", status_code=200)(view_course)
    router.post("/new", status_code=201)(create_course)
    router.put("/status/{course_id}", status_code = 200)(switch_course_status)
    router.delete("/", status_code=204)(course_delete)
    router.get("/ratings/{course_id}", status_code=200)(view_ratings)