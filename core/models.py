import uuid
from django.db import models
from django.contrib.auth.models import User


# =====================
# Teacher
# =====================

class Teacher(models.Model):
    idTeacher = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.TextField(
        'Full name',
        max_length=100
    )

    email = models.EmailField(
        'Email',
        max_length=100
    )

    dateOfBirth = models.DateField(
        'Date of birth'
    )

    gender = models.CharField(
        max_length=1
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'


# ====================
# Student
# ====================

class Student(models.Model):
    idStudent = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.TextField(
        'Full name',
        max_length=100
    )

    email = models.EmailField(
        'Email',
        max_length=100
    )

    dateOfBirth = models.DateField(
        'Date of birth'
    )

    gender = models.CharField(
        max_length=1
    )

    course = models.CharField(
        'Course',
        max_length=100
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
