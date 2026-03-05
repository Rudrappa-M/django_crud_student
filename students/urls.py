from django.urls import path

from .views import (
    create_student,
    delete_student,
    read_student_by_id,
    read_students,
    update_student,
)

urlpatterns = [
    path("students/create/", create_student, name="create-student"),
    path("students/read/", read_students, name="read-students"),
    path("students/read/<int:student_id>/", read_student_by_id, name="read-student-by-id"),
    path("students/update/<int:student_id>/", update_student, name="update-student"),
    path("students/delete/<int:student_id>/", delete_student, name="delete-student"),
]
