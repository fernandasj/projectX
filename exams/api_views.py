from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import uuid
from datetime import datetime
from . import tasks
from Docker import main
from . import models as exams
from . import serializers

from .data_objects import QuestionAnswer, TestResult

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
        question = exams.Question.objects.create(headQuestion=request.data['headQuestion'], typeQuestion=int(request.data['typeQuestion']), discipline_id=request.data['discipline'])
        print(question.typeQuestion)
        if question.typeQuestion == 0:
            print("CHOICES")
            for choice in request.data['choices']:
                newChoice = exams.Choice.objects.create(question=question, correct=choice['correct'], 
                    textChoice=choice['textChoice'])
                newChoice.save()
        elif question.typeQuestion == 2:
            print("CODES")
            codeAnswer = exams.CodeAnswer.objects.create(question=question, inputCode=request.data['input'], outputCode=request.data['output'])
            codeAnswer.save()
            # print(request.data['input'], request.data['output'])
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

    # @action(detail=True, methods=['GET'], name='Attach meta items ids')
    # def studentResult(self, request, pk=None):
    #     queryset = exams.TestStudent.objects.filter(student_id=pk)
    #     serializer = serializers.TestStudentSerializer(queryset, many=True)
    #     return Response(serializer.data)

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
            return serializers.AnswerSerializer
        return super().get_serializer_class()


# ======================
# TestStudent
# ======================
class TestStudentViewSet(viewsets.ModelViewSet):

    queryset = exams.TestStudent.objects.filter(active=True)
    serializer_class = serializers.CreateTestStudentSerializer

    def create(self, request):
        now = datetime.now()
        testStudent = exams.TestStudent.objects.create(test_id=request.data['test'], student_id=request.data['student'], timeFinish=request.data['timeFinish'])
        testStudent.timeStart = testStudent.test.aplicationDate
        testStudent.scores = 0
        questions = testStudent.test.questions.count()
        scoreQuestion = 100 / questions

        answers = exams.Answer.objects.filter(student=testStudent.student)
        for answer in answers:
            if answer.correct:
                testStudent.scores += scoreQuestion

        testStudent.save()
        return Response({'id': testStudent.pk ,'status': '200'})


    @action(detail=True, methods=['GET'], name='get test with question and answer')
    def result(self, request, pk=None):
       
        test_student = exams.TestStudent.objects.get(pk=pk)
        questions = list(test_student.test.questions.all())
        answers = list(exams.Answer.objects.filter(
            test=test_student.test,
            student=test_student.student
        ))

        data = TestResult(
            idTest=test_student.idTestStudent,
            name=test_student.test.name,
            discipline=test_student.test.discipline.name,
            scores=test_student.scores,
            student=test_student.student.name,
            questions=[
                QuestionAnswer(headQuestion=q.headQuestion, typeQuestion=q.get_typeQuestion_display, correctAnswer=a.correct)
                for q in questions
                for a in answers
                if a.question.pk == q.pk
            ]
        )
        
        serializer = serializers.TestResultSerializer(data)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.method.lower() == 'get':
            return serializers.TestStudentSerializer
        return super().get_serializer_class()