from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from . import models
from . import serializers


# ======================
# Discipline
# ======================

@api_view(["GET"])
def discipline_list(request):
   disciplines = Discipline.objects.all()
    serializer = DisciplineSerializer(disciplines, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def discipline_detail(request, id):
    try:
        discipline = Discipline.objects.get(id=id)
        serializer = DisciplineSerializer(discipline)
        return Response(serializer.data)
    except Discipline.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


# ======================
# Question
# ======================

@api_view(["GET"])
def question_list(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def question_detail(request, id):
    try:
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    except Question.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


# ======================
# Test
# ======================

@api_view(["GET"])
def test_list(request):
   tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def test_detail(request, id):
    try:
        test = Test.objects.get(id=id)
        serializer = TestSerializer(test)
        return Response(serializer.data)
    except Test.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


# ======================
# CodeAnswer
# ======================

@api_view(["GET"])
def codeAnswer_list(request):
    codeAnswers = CodeAnswer.objects.all()
    serializer = CodeAnswerSerializer(codeAnswers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def codeAnswer_detail(request, id):
    try:
        codeAnswer = CodeAnswer.objects.get(id=id)
        serializer = CodeAnswerSerializer(test)
        return Response(serializer.data)
    except CodeAnswer.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


# ======================
# Choice
# ======================

@api_view(["GET"])
def choice_list(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def choice_detail(request, id):
    try:
        choice = Choice.objects.get(id=id)
        serializer = ChoiceSerializer(choice)
        return Response(serializer.data)
    except Choice.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)


# ======================
# Answer
# ======================

@api_view(["GET"])
def answer_list(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def answer_detail(request, id):
    try:
        answer = Answer.objects.get(id=id)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)
    except Answer.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)



# ======================
# TestStudent
# ======================

@api_view(["GET"])
def testStudent_list(request):
    testStudents = TestStudent.objects.all()
    serializer = TestStudentSerializer(testStudents, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def testStudent_detail(request, id):
    try:
        testStudent = TestStudent.objects.get(id=id)
        serializer = testStudentSerializer(testStudent)
        return Response(serializer.data)
    except TestStudent.DoesNotExist:
        return Response({}, status=status.HTTP_404_NOT_FOUND)

