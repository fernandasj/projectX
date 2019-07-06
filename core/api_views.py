from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer

from . import models
from . import serializers


# Auth token viewset
# - - - - - - - - - - - - - - - - - - -
class AuthToken(ObtainAuthToken):

    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        if user.teachers:
            result = serializers.TeacherSerializer(user.teachers)
        else:
            result = serializers.StudentSerializer(user.students)

        return Response(result.data)


# Teacher
# - - - - - - - - - - - - - - - - - - -
class TeacherViewSet(viewsets.ModelViewSet):

    queryset = models.Teacher.objects.filter(active=True)
    serializer_class = serializers.TeacherSerializer


# Student
# - - - - - - - - - - - - - - - - - - -
class StudentViewSet(viewsets.ModelViewSet):

    queryset = models.Student.objects.filter(active=True)
    serializer_class = serializers.StudentSerializer