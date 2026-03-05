from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer


@swagger_auto_schema(method="post", request_body=StudentSerializer)
@api_view(["POST"])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def read_students(request):
    students = Student.objects.all().order_by("id")
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def read_student_by_id(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method="put", request_body=StudentSerializer)
@swagger_auto_schema(method="patch", request_body=StudentSerializer)
@api_view(["PUT", "PATCH"])
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    partial = request.method == "PATCH"
    serializer = StudentSerializer(student, data=request.data, partial=partial)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return Response(
        {"message": "Student deleted successfully"},
        status=status.HTTP_204_NO_CONTENT,
    )
