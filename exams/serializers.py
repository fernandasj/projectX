from rest_framework import serializers
from . import models
from core import serializers as core

# ======================
# Discipline
# ======================
class DisciplineSerializer(serializers.ModelSerializer):
    
    teacher = core.TeacherSerializer()    
    students = core.StudentSerializer(many=True)
    
    class Meta:
        model = models.Discipline
        fields = ('name', 'teacher', 'students')


class CreateDisciplineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Discipline
        fields = ('name', 'teacher', 'students')
        list_serializer_class = DisciplineSerializer


# ======================
# Question
# ======================
class QuestionSerializer(serializers.HyperlinkedModelSerializer):


    discipline = DisciplineSerializer(
        many=False,
        read_only=True,
        )

    class Meta:
        model = models.Question
        fields = ('idQuestion', 'headQuestion', 'typeQuestion', 'discipline')


# ======================
# Test
# ======================
class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'


# ======================
# CodeAnsewer
# ======================
class CodeAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CodeAnswer
        fields = '__all__'


# ======================
# Choice
# ======================
class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'


# ======================
# Answer
# ======================
class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'


# ======================
# TestStudent
# ======================
class TestStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TestStudent
        fields = '__all__'