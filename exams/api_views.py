from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import uuid
from . import tasks
from Docker import main
from . import models as exams
from . import serializers

# ======================
# Discipline
# ======================
class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = exams.Discipline.objects.filter(active=True)
    serializer_class = serializers.DisciplineSerializer

# ======================
# Question
# ======================
class QuestionCreateView(viewsets.ViewSet):

    def create(self, request):
        print(request)

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = exams.Question.objects.filter(active=True)
    serializer_class = serializers.CreateQuestionSerializer

    @action(detail=True, methods=['GET'], name='Attach meta items ids')
    def choices(self, request, pk=None):
        queryset = exams.Choice.objects.filter(question_id=pk)
        serializer = serializers.ChoiceSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'], name='Attach meta items ids')
    def codes(self, request, pk=None):
        queryset = exams.CodeAnswer.objects.filter(question_id=pk)
        serializer = serializers.CodeAnswerSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        question = exams.Question.objects.create(headQuestion=request.data['headQuestion'], typeQuestion=request.data['typeQuestion'], discipline_id=request.data['discipline'])
        if question.typeQuestion == '0':
            print(request.data['choices'])
            for choice in request.data['choices']:
                newChoice = exams.Choice.objects.create(question=question, correct=choice['correct'], 
                    textChoice=choice['textChoice'])
                newChoice.save()
        elif question.typeQuestion == '2':
            codeAnswer = exams.CodeAnswer.objects.create(question=question, inputCode=request.data['input'], outputCode=request.data['output'])
            codeAnswer.save()
            print(request.data['input'], request.data['output'])
        question.save()
        return Response({'status': '200'})

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

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.CodeAnswerSerializer
        return super().get_serializer_class()

# ======================
# Choice
# ======================
class ChoiceViewSet(viewsets.ModelViewSet):

    queryset = exams.Choice.objects.filter(active=True)
    serializer_class = serializers.CreateChoiceSerializer

    @action(detail=True, methods=['GET'], name='Attach meta items ids')
    def custom_action(self, request, pk=None):
        queryset = exams.Choice.objects.filter(question_id=pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.ChoiceSerializer
        return super().get_serializer_class()



# ======================
# Answer
# ======================
class AnswerViewSet(viewsets.ModelViewSet):

    queryset = exams.Answer.objects.filter(active=True)
    serializer_class = serializers.CreateAnswerSerializer

    def create(self, request):
        answer = exams.Answer.objects.create(textAnswer=request.data['textAnswer'], student_id=request.data['student'], test_id=request.data['test'], question_id=request.data['question'])
        if answer.question.typeQuestion == 0:
            answer.choice_pk = request.data['choice']
            tasks.correctionChoice(answer.choice_pk, answer.pk)

        elif answer.question.typeQuestion == 2:
            tasks.correctionCode(answer.pk)
        answer.save()
        return Response({'status': '200'})

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            tasks.image()
            return serializers.AnswerSerializer
        return super().get_serializer_class()


# ======================
# TestStudent
# ======================
class TestStudentViewSet(viewsets.ModelViewSet):

    queryset = exams.TestStudent.objects.filter(active=True)
    serializer_class = serializers.CreateTestStudentSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.TestStudentSerializer
        return super().get_serializer_class()