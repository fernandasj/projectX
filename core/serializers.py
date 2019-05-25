from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
	
	# user=User(
 #        many=False,
 #        read_only=True
 #    )
    
    class Meta:
        model = models.Teacher
        fields = ('idTeacher','name', 'email', 'dateOfBirth', 'gender')
        

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')
