import uuid
from django.db import models
from django.contrib.auth.models import User


# =====================
# Teacher
# =====================

class Teacher(models.Model):
    M = 'M'
    F = 'F'
    GENDER = (
        (M, 'M'),
        (F, 'F'),
    )

    idTeacher = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
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
        choices=GENDER,
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='teachers'
    )

    active = models.BooleanField(
        default=True
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
    SELECT = 'SELECT'
    M = 'M'
    F = 'F'
    GENDER = (
        (SELECT, 'SELECT'),
        (M, 'M'),
        (F, 'F'),
    )
    
    idStudent = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
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
        'Gender',
        max_length=1,
        choices=GENDER,
        default=SELECT
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

    active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
