from datetime import date

from models import Course, DBCourse, Location, CourseDay
from database import db_session

def make_course(db_course):
    return Course(
        name=db_course.name,
        slug=db_course.slug,
        description=db_course.description,
        days=[(d.name, d.start_time, d.end_time) for d in db_course.days],
        start_date=db_course.start_date,
        end_date=db_course.end_date,
        location=db_course.location.name,
        cost=db_course.cost,
        has_space=db_course.has_space,
        map_image=db_course.location.map_image,
        map_url=db_course.location.map_url,
        drop_in_open=db_course.drop_in_open,
        drop_in_fee=db_course.drop_in_fee,
        note=db_course.note,
        partial_attendance=db_course.partial_attendance,
        allow_assessments=db_course.allow_assessments,
    )

all_db_courses = db_session.query(DBCourse).all()
all_courses = [make_course(db_course) for db_course in all_db_courses]

class CurrentCourseIterator(object):
    def all_courses(self):
        all_db_courses = db_session.query(DBCourse).all()
        return [make_course(db_course) for db_course in all_db_courses]
    def __iter__(self):
        return (course for course in self.all_courses() if not course.completed())

current_courses = CurrentCourseIterator()
