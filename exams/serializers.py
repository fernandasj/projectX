from rest_framework import serializers
from . import models
from core import serializers as core


class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    
    teacher = core.TeacherSerializer(
        many=False,
        read_only=True,
        )
    
    students = core.StudentSerializer(
        many=True,
        read_only=True,
        )
    
    class Meta:
        model = models.Discipline
        fields = ('name', 'teacher', 'students')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):


    discipline = DisciplineSerializer(
        many=False,
        read_only=True,
        # source='name',
        # view_name="Discipline-detail"
        )

    class Meta:
        model = models.Question
        fields = ('idQuestion', 'headQuestion', 'typeQuestion', 'discipline')


class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = '__all__'


class CodeAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.CodeAnswer
        fields = '__all__'


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Choice
        fields = '__all__'


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'



class TestStudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.TestStudent
        fields = '__all__'