from rest_framework import serializers
from . import models as exams
from core import serializers as core


# ======================
# Discipline
# ======================
class DisciplineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = exams.Discipline
        fields = ('idDiscipline','name', 'teacher', 'students')


class CreateDisciplineSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = exams.Discipline
        fields = ('idDiscipline','name', 'teacher', 'students')
        # list_serializer_class = DisciplineSerializer


# ======================
# Question
# ======================
class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Question
        fields = ('idQuestion', 'headQuestion', 'typeQuestion', 'get_typeQuestion_display', 'discipline')
       

class CreateQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = exams.Question
        fields = ('idQuestion', 'headQuestion', 'typeQuestion', 'discipline')

# ======================
# Test
# ======================
class TestSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(many=True)
    discipline = serializers.StringRelatedField(many=False)
    aplicationDate = serializers.DateTimeField(format='%d/%m/%Y')
    aplicationDateLimit = serializers.DateTimeField(format='%d/%m/%Y')

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

    # choice = ChoiceSerializer(default="")

    class Meta:
        model = exams.Answer
        fields = ('idAnswer', 'textAnswer', 'correct', 'choice', 'student', 'test', 'question')
        list_serializer_class = AnswerSerializer


# ======================
# TestStudent
# ======================
class TestStudentSerializer(serializers.ModelSerializer):

    test = TestSerializer(read_only=True)
    student = core.StudentSerializer(read_only=True)
    
    class Meta:
        model = exams.TestStudent
        fields = ('idTestStudent', 'test', 'student', 'scores', 'timeStart', 'timeFinish')


class CreateTestStudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = exams.TestStudent
        fields = ('idTestStudent', 'test', 'student', 'scores', 'timeStart', 'timeFinish')
        list_serializer_class = TestStudentSerializer