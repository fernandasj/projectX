from rest_framework import serializers
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User

from . import models


class TeacherSerializer(serializers.ModelSerializer):

    pk = serializers.UUIDField(read_only=True, source='idTeacher')
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username já cadastrado.")
        return value

    def create(self, validated_data):
        username = validated_data.pop('username')

        user = User.objects.create(username=username, first_name=validated_data['name'], email=validated_data['email'])
        user.set_password(validated_data.pop('password'))
        user.save()

        teacher = models.Teacher.objects.create(**validated_data, user=user)
        return teacher

    class Meta:
        model = models.Teacher
        fields = ('pk', 'name', 'email', 'dateOfBirth', 'gender', 'username', 'password', 'token')
        

class StudentSerializer(serializers.ModelSerializer):

    pk = serializers.UUIDField(read_only=True, source='idStudent')
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username já cadastrado.")
        return value

    def create(self, validated_data):
        username = validated_data.pop('username')

        user = User.objects.create(username=username, first_name=validated_data['name'], email=validated_data['email'])
        user.set_password(validated_data.pop('password'))
        user.save()

        teacher = models.Student.objects.create(**validated_data, user=user)
        return teacher

    class Meta:
        model = models.Student
        fields = ('pk', 'name', 'email', 'dateOfBirth', 'course', 'gender', 'username', 'password', 'token')


# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name', 'password', 'is_superuser')
