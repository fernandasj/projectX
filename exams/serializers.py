from rest_framework import serializers
from . import models


class DisciplineSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Discipline
        fields = '__all__'


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'


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