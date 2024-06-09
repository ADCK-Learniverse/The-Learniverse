from typing import Annotated

from fastapi import APIRouter, Depends, Query
from backend.app.models import Course
from backend.app.api.services.login_services import get_current_user
from backend.app.api.services.course_services import (new_course, switch_status, subscribe,
                                                      delete_course, unsubscribe, rate, view_all,
                                                      view_particular, show_ratings, check_for_subscription,
                                                      get_pic_for_frontend, check_for_rating_frontend)
import logging

course_router = APIRouter(prefix="/courses")

user_dependency = Annotated[dict, Depends(get_current_user)]



@course_router.get("/all", status_code=200)
def view_all_courses(
    search: str = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """This method returns a list with all courses,
    provides the option to search for a specific value, and allows pagination."""

    return view_all(search, page, size)


@course_router.get("/{course_id}", status_code=200)
def view_course(user: user_dependency, course_id: int):

    """This method requires a course_id and returns the course with its entire information if it's there."""

    user_id = user.get("id")
    user_role = user.get("role")
    return view_particular(course_id, user_id, user_role)


@course_router.post("/new", status_code=201)
def create_course(user: user_dependency, course: Course):

    """This method uses the init method to create a new object with the inserted values for verifications
    and creates a new course inside the database with the values."""

    logging.debug(user)
    user_id = user.get("id")
    user_role = user.get("role")
    return new_course(user_id, user_role, course)


@course_router.put("/status/{course_id}", status_code=200)
def switch_course_status(user: user_dependency, course_id: int):

    """This method requires the id of the course to switch the status of the course between public and premium."""

    user_role = user.get("role")
    user_id = user.get("id")
    return switch_status(course_id, user_role, user_id)


@course_router.get("/subscription/check_for_subscription/{course_id}", status_code=200)
def check_for_sub(user: user_dependency, course_id: int):

    """This method requires the course id for which the user wants to subscribe
     and subscribes him by inserting a new entry inside the database."""

    user_id = user.get("id")
    return check_for_subscription(user_id, course_id)


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

    """This method requires the course_id and removes the desired course from the database."""

    user_id = user.get("id")
    user_role = user.get("role")
    return delete_course(user_id, user_role, course_id)


@course_router.post("/rating/{course_id}", status_code=201)
def rate_course(user: user_dependency, course_id: int, rating: int = Query(gt=0, lt=11)):

    """This method requires course_id and the desired rating, and once submitted,
    recalculates and updates the course's rating."""
    user_id = user.get("id")
    return rate(user_id, course_id, rating)


@course_router.get("/ratings/{course_id}", status_code=200)
def view_ratings(user: user_dependency, course_id: int, page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)):

    """This method requires course_id, offers pagination features, and returns the ratings given to the specific course."""
    return show_ratings(course_id)


def course_related_endpoints(router: APIRouter):
    router.get("/all", status_code=200)(view_all_courses)
    router.get("/{course_id}", status_code=200)(view_course)
    router.post("/new", status_code=201)(create_course)
    router.put("/status/{course_id}", status_code = 200)(switch_course_status)
    router.delete("/", status_code=204)(course_delete)
    router.get("/ratings/{course_id}", status_code=200)(view_ratings)