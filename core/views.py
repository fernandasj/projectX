from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer


# ======================
# Student
# ======================

@api_view(["GET"])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def student_detail(request, id):
    try:
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

# ======================
# Teacher
# ======================

@api_view(["GET"])
def teacher_list(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def teacher_detail(request, id):
    try:
        teacher = Teacher.objects.get(id=id)
        serializer = StudentSerializer(teacher)
        return Response(serializer.data)
    except Teacher.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)