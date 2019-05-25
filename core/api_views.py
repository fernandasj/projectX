from rest_framework import viewsets, permissions

from . import models
from . import serializers

class TeacherViewSet(viewsets.ModelViewSet):

    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer