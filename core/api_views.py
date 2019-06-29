from rest_framework import viewsets, permissions

from . import models
from . import serializers

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = models.Teacher.objects.filter(active=True)
    serializer_class = serializers.TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.filter(active=True)
    serializer_class = serializers.StudentSerializer