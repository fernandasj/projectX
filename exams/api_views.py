from rest_framework import viewsets, permissions

from . import models as exams
from . import serializers

# ======================
# Discipline
# ======================
class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = exams.Discipline.objects.all()
    serializer_class = serializers.DisciplineSerializer

    class Meta:
        list_serializer_class = serializers.DisciplineSerializer


# ======================
# Question
# ======================
class QuestionViewSet(viewsets.ModelViewSet):

    queryset = exams.Question.objects.all()
    serializer_class = serializers.CreateQuestionSerializer

    class Meta:
        list_serializer_class = serializers.QuestionSerializer


# ======================
# Test
# ======================
class TestViewSet(viewsets.ModelViewSet):

    queryset = exams.Test.objects.all()
    serializer_class = serializers.CreateTestSerializer

    class Meta:
        list_serializer_class = serializers.TestSerializer


# ======================
# CodeAnswer
# ======================
class CodeAnswerViewSet(viewsets.ModelViewSet):

    queryset = exams.CodeAnswer.objects.all()
    serializer_class = serializers.CreateCodeAnswerSerializer

    class Meta:
        list_serializer_class = serializers.CodeAnswerSerializer


# ======================
# Choice
# ======================
class ChoiceViewSet(viewsets.ModelViewSet):

    queryset = exams.Choice.objects.all()
    serializer_class = serializers.CreateChoiceSerializer

    class Meta:
        list_serializer_class = serializers.ChoiceSerializer


# ======================
# Answer
# ======================
class AnswerViewSet(viewsets.ModelViewSet):

    queryset = exams.Answer.objects.all()
    serializer_class = serializers.CreateAnswerSerializer

    class Meta:
        list_serializer_class = serializers.AnswerSerializer


# ======================
# TestStudent
# ======================
class TestStudentViewSet(viewsets.ModelViewSet):

    queryset = exams.TestStudent.objects.all()
    serializer_class = serializers.CreateTestStudentSerializer

    class Meta:
        list_serializer_class = serializers.TestStudentSerializer
        