"""
PROJECT: The School Management System

Goal: Use SQLAlchemy to build a persistent management system for a school.

Requirements:

1. Models:
   - 'Student': 'id', 'name', 'email'.
   - 'Course': 'id', 'title', 'instructor'.

2. Features (Functions using Session):
   - 'register_student(name, email)': Creates a new student.
   - 'create_course(title, instructor)': Creates a new course.
   - 'enroll_student_in_course(student_id, course_id)': (Advanced: requires a many-to-many relationship OR a simple 'Course' foreign key on the Student).
   - 'list_all_students()': Prints a formatted list of all students.

3. Testing:
   - Add 3 students.
   - Add 2 courses.
   - Query students by name to verify they exist.

Real-World Logic:
- This is how large-scale enterprise apps are built. Instead of writing 1,000 strings of SQL, developers manage everything through clean Python classes and relationships.
"""

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
    Table
)

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    relationship
)

import os

# ======================================
# DATABASE SETUP
# ======================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_PATH = f"sqlite:///{os.path.join(BASE_DIR, 'school.db')}"

engine = create_engine(DB_PATH, echo=False)

Base = declarative_base()

Session = sessionmaker(bind=engine)


# ======================================
# MANY-TO-MANY ASSOCIATION TABLE
# ======================================

student_course = Table(
    "student_course",
    Base.metadata,

    Column(
        "student_id",
        Integer,
        ForeignKey("students.id")
    ),

    Column(
        "course_id",
        Integer,
        ForeignKey("courses.id")
    )
)


# ======================================
# MODELS
# ======================================

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    # Relationship
    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students" # this means that the courses table will have a student attribute
    )

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', email='{self.email}')>"


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)

    title = Column(String, nullable=False)

    instructor = Column(String, nullable=False)

    # Relationship
    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses" # this means that the students table will have a courses attribute
    )

    def __repr__(self):
        return f"<Course(id={self.id}, title='{self.title}')>"


# ======================================
# CREATE TABLES
# ======================================

Base.metadata.create_all(engine)


# ======================================
# FUNCTIONS
# ======================================

def register_student(session, name, email):
    student = Student(
        name=name,
        email=email
    )

    session.add(student)

    session.commit()

    print(f"Student '{name}' registered successfully.")

    return student


def create_course(session, title, instructor):
    course = Course(
        title=title,
        instructor=instructor
    )

    session.add(course)

    session.commit()

    print(f"Course '{title}' created successfully.")

    return course


def enroll_student_in_course(session, student_id, course_id):

    student = session.query(Student).filter_by(
        id=student_id
    ).first()

    course = session.query(Course).filter_by(
        id=course_id
    ).first()

    if not student:
        print("Student not found.")
        return

    if not course:
        print("Course not found.")
        return

    student.courses.append(course)

    session.commit()

    print(f"{student.name} enrolled in {course.title}")


def list_all_students(session):

    students = session.query(Student).all()

    print("\n===== ALL STUDENTS =====")

    for student in students:

        print(f"ID: {student.id}")
        print(f"Name: {student.name}")
        print(f"Email: {student.email}")

        if student.courses:
            print("Courses:")

            for course in student.courses:
                print(f" - {course.title}")

        else:
            print("Courses: None")

        print("-" * 30)


def find_student_by_name(session, name):

    students = session.query(Student).filter(
        Student.name == name
    ).all()

    return students


# ======================================
# MAIN PROGRAM
# ======================================

def main():

    session = Session()

    try:

        # ------------------------------
        # ADD STUDENTS
        # ------------------------------

        s1 = register_student(
            session,
            "Hamza",
            "hamza@example.com"
        )

        s2 = register_student(
            session,
            "Ali",
            "ali@example.com"
        )

        s3 = register_student(
            session,
            "Sara",
            "sara@example.com"
        )

        # ------------------------------
        # ADD COURSES
        # ------------------------------

        c1 = create_course(
            session,
            "Python Programming",
            "Dr. Ahmed"
        )

        c2 = create_course(
            session,
            "Database Systems",
            "Prof. Khan"
        )

        # ------------------------------
        # ENROLLMENTS
        # ------------------------------

        enroll_student_in_course(
            session,
            s1.id,
            c1.id
        )

        enroll_student_in_course(
            session,
            s1.id,
            c2.id
        )

        enroll_student_in_course(
            session,
            s2.id,
            c1.id
        )

        # ------------------------------
        # LIST STUDENTS
        # ------------------------------

        list_all_students(session)

        # ------------------------------
        # SEARCH BY NAME
        # ------------------------------

        print("\n===== SEARCH RESULTS =====")

        students = find_student_by_name(
            session,
            "Hamza"
        )

        for student in students:
            print(student)

    except InterruptedError as e:
        print("Student with this email already exists.")
        session.rollback()
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()

    finally:

        session.close()


if __name__ == "__main__":
    main()
