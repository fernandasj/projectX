from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Teacher
        fields = ('idTeacher','name', 'email', 'dateOfBirth', 'gender', 'user')
        

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = ('idStudent','name', 'email', 'dateOfBirth', 'course', 'gender', 'user')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')
