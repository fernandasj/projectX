from rest_framework import serializers
from . import models as exams
from core import serializers as core


# ======================
# Discipline
# ======================
class DisciplineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = exams.Discipline
        fields = ('name', 'teacher', 'students')


class CreateDisciplineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = exams.Discipline
        fields = ('name', 'teacher', 'students')
        list_serializer_class = DisciplineSerializer


# ======================
# Question
# ======================
class QuestionSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()

    def get_type(self, obj):
        return exams.Question.TYPE_QUESTION[obj.typeQuestion][1]

    class Meta:
        model = exams.Question
        fields = ('idQuestion', 'headQuestion', 'type', 'discipline')
       

class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Question
        fields = ('idQuestion', 'headQuestion', 'typeQuestion', 'discipline')

# ======================
# Test
# ======================
class TestSerializer(serializers.ModelSerializer):

    # discipline = DisciplineSerializer()
    # questions = QuestionSerializer(many=True)

    class Meta:
        model = exams.Test
        fields = ('idTest', 'aplicationDate', 'aplicationDateLimit', 'name', 'discipline', 'questions')


class CreateTestSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Test
        fields = ('idTest', 'aplicationDate', 'aplicationDateLimit', 'name', 'discipline', 'questions')


# ======================
# CodeAnswer
# ======================
class CodeAnswerSerializer(serializers.ModelSerializer):

    question = QuestionSerializer(read_only=True)

    class Meta:
        model = exams.CodeAnswer
        fields = ('idCodeAnswer', 'question', 'inputCode', 'outputCode')


class CreateCodeAnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = exams.CodeAnswer
        fields = ('idCodeAnswer', 'question', 'inputCode', 'outputCode')
        list_serializer_class = CodeAnswerSerializer


# ======================
# Choice
# ======================
class ChoiceSerializer(serializers.ModelSerializer):

    # question = QuestionSerializer()

    class Meta:
        model = exams.Choice
        fields = ('idChoice', 'question', 'correct', 'textChoice')


class CreateChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Choice
        fields = ('idChoice', 'question', 'correct', 'textChoice')
        list_serializer_class = ChoiceSerializer


# ======================
# Answer
# ======================
class AnswerSerializer(serializers.ModelSerializer):

    # student = core.StudentSerializer()
    # test = TestSerializer()
    # question = QuestionSerializer()

    class Meta:
        model = exams.Answer
        fields = ('idAnswer', 'textAnswer', 'correct', 'choice', 'student', 'test', 'question')


class CreateAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Answer
        fields = ('idAnswer', 'textAnswer', 'correct', 'choice', 'student', 'test', 'question')
        list_serializer_class = AnswerSerializer


# ======================
# TestStudent
# ======================
class TestStudentSerializer(serializers.ModelSerializer):

    # test = TestSerializer()
    # student = core.StudentSerializer()
    
    class Meta:
        model = exams.TestStudent
        fields = ('idTestStudent', 'test', 'student', 'scores', 'timeStart', 'timeFinish')


class CreateTestStudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = exams.TestStudent
        fields = ('idTestStudent', 'test', 'student', 'scores', 'timeStart', 'timeFinish')
        list_serializer_class = TestSerializer