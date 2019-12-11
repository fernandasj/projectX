from rest_framework import viewsets, permissions

from . import models as exams
from . import serializers

# ======================
# Discipline
# ======================
class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = exams.Discipline.objects.filter(active=True)
    serializer_class = serializers.DisciplineSerializer

    class Meta:
        list_serializer_class = serializers.DisciplineSerializer


# ======================
# Question
# ======================
class QuestionViewSet(viewsets.ModelViewSet):

    queryset = exams.Question.objects.filter(active=True)
    serializer_class = serializers.CreateQuestionSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.QuestionSerializer
        return super().get_serializer_class()


# ======================
# Test
# ======================
class TestViewSet(viewsets.ModelViewSet):

    queryset = exams.Test.objects.filter(active=True)
    serializer_class = serializers.CreateTestSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.TestSerializer
        return super().get_serializer_class()


# ======================
# CodeAnswer
# ======================
class CodeAnswerViewSet(viewsets.ModelViewSet):

    queryset = exams.CodeAnswer.objects.filter(active=True)
    serializer_class = serializers.CreateCodeAnswerSerializer

    class Meta:
        list_serializer_class = serializers.CodeAnswerSerializer


# ======================
# Choice
# ======================
class ChoiceViewSet(viewsets.ModelViewSet):

    queryset = exams.Choice.objects.filter(active=True)
    serializer_class = serializers.CreateChoiceSerializer

    class Meta:
        list_serializer_class = serializers.ChoiceSerializer


# ======================
# Answer
# ======================
class AnswerViewSet(viewsets.ModelViewSet):

    queryset = exams.Answer.objects.filter(active=True)
    serializer_class = serializers.CreateAnswerSerializer

    class Meta:
        list_serializer_class = serializers.AnswerSerializer


# ======================
# TestStudent
# ======================
class TestStudentViewSet(viewsets.ModelViewSet):

    queryset = exams.TestStudent.objects.filter(active=True)
    serializer_class = serializers.CreateTestStudentSerializer

    class Meta:
        list_serializer_class = serializers.TestStudentSerializer
        