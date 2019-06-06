from rest_framework import viewsets, permissions

from . import models
from . import serializers

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer