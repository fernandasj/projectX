from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# from . import tasks
from Docker import main
from . import models as exams
from . import serializers

# ======================
# Discipline
# ======================
class DisciplineViewSet(viewsets.ModelViewSet):

    queryset = exams.Discipline.objects.filter(active=True)
    serializer_class = serializers.DisciplineSerializer

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            # r = tasks.add(1, 3)
            r = main.build_image()
            r(blocking=False)
            print("aqui")
            # print("TASK - " + str(r(blocking=True)))
            return serializers.DisciplineSerializer
        return super().get_serializer_class()


# ======================
# Question
# ======================
class QuestionCreateView(viewsets.ViewSet):
    # """docstring for DisciplineCreateView"""
    # def __init__(self, arg):
    #     super(DisciplineCreateView, self).__init__()
    #     self.arg = arg


    def create(self, request):
        print(request)

class QuestionViewSet(viewsets.ModelViewSet):

    queryset = exams.Question.objects.filter(active=True)
    serializer_class = serializers.CreateQuestionSerializer

    @action(detail=False, methods=['POST'])
    def test(self, request):
        print("oi")
        question = exams.Question.objects.create(headQuestion=request.data['headQuestion'], 
            typeQuestion=request.data['typeQuestion'], discipline=request.data['discipline'])
        print(question.typeQuestion)
        if question.typeQuestion == 0:
            for choice in choices:
                newChoice = exams.Choice.objects.create(question=question.idQuestion, correct=request.data['correct'], 
                    textChoice=request.data['textChoice'])
                newChoice.save()
        elif question.typeQuestion == 2:
            # for code in request.data['codeList']:
            #     newCode = exams.CodeAnswer.create(question=question.idQuestion, inputCode=code['input'], 
            #         outputCode=code['output'])
            #     print('CODE: ' + newCode)
            #     newCode.save()
            #     print('passou')

            newCode = exams.CodeAnswer.create(question=question.idQuestion, inputCode=resquest.data['input'], 
                outputCode=request.data['output'])
            newCode.save()
            question.save()

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

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.TestStudentSerializer
        return super().get_serializer_class()