from backend.app.data.database import read_query
from backend.app.api.services.register_services import send_emails


def new_course_newsletter(topic):
    subscribers = read_query('SELECT email FROM newsletter')
    send_emails(subscribers[0],
                'Courses', f"A new course regarding {topic} has been released!",
                "<h3>A new course is waiting for you.</h3>")


def removed_course_newsletter():
    subscribers = read_query('SELECT email FROM newsletter')
    send_emails(subscribers[0],
                'Courses', f"A Course has been removed from our platform!",
                "<h3>No longer a part of the Learniverse.</h3>")