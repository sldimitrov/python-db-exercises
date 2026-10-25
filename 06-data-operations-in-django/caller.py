import os
import django
from datetime import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Student

data = [
    {
        "student_id": "FC5204",
        "first_name": "John",
        "last_name": "Doe",
        "birth_date": "15/05/1995",
        "email": "john.doe@university.com"
    },
    {
        "student_id": "FE0054",
        "first_name": "Jane",
        "last_name": "Smith",
        "birth_date": None,
        "email": "jane.smith@university.com"
    },
    {
        "student_id": "FH2014",
        "first_name": "Alice",
        "last_name": "Johnson",
        "birth_date": "18/02/1998",
        "email": "alice.johnson@university.com"
    },
    {
        "student_id": "FH2015",
        "first_name": "Bob",
        "last_name": "Wilson",
        "birth_date": "25/11/1996",
        "email": "bob.wilson@university.com"
    }
]


def add_students():
    for d in data:
        if d["birth_date"]:
            d["birth_date"] = datetime.strptime(d["birth_date"], "%d/%m/%Y").date()

        student = Student.objects.create(**d)
        student.save()

    return "Students added successfully!"


def get_students_info():
    students = Student.objects.all()

    results = []

    for student in students:
        results.append(
            f"Student {student.student_id}: {student.first_name} {student.last_name}; Email: {student.email}")

    return "\n".join(results)


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        if student.email and "@" in student.email:
            username, old_domain = student.email.split("@")

            if old_domain != "uni-students.com":
                student.email = student.email
                # Update the field
                student.email = f"{username}@uni-students.com"

                student.save()
                print(f"Updated email to: {student.email}")

    print("Students emails updated successfully!")


def truncate_students():
    students = Student.objects.all()

    for student in students:
        student.delete()


# Run the function when executing caller.py directly
if __name__ == "__main__":
    # update_students_emails()
    print(get_students_info())
    # truncate_students()
