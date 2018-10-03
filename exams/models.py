import uuid
from django.db import models
from core.models import Student, Teacher


# ======================
# Question
# ======================

class Question(models.Model):
    CODE = 'CODE'
    OBJECTIVE = 'OBJECTIVE'
    SUBJECTIVE = 'SUBJECTIVE'
    TYPE_QUESTION = (
        (CODE, 'Code'),
        (SUBJECTIVE, 'Subjective'),
        (OBJECTIVE, 'Objective'),
    )

    idQuestion = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    headQuestion = models.CharField(
        'Head Question',
        max_length=500
    )

    typeQuestion = models.CharField(
        'Type Question',
        max_length=45,
        choices=TYPE_QUESTION,
        default=OBJECTIVE
    )


    discipline = models.ForeignKey(
        'Discipline',
        Discipline,
        verbose_name='discipline',
        related_name='questions'
    )

    def __str__(self):
        return self.headQuestion

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


# ======================
# Test
# ======================

class Test(models.Model):
    idTest = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    aplicationDate = models.DateTimeField(
        'Aplication Date'
    )

    aplicationDateLimit = models.DateTimeField(
        'Aplication Date Limit'
    )

    name = models.TextField(
        'Text name',
        max_length=254
    )

    discipline = models.ForeignKey(
        'Discipline',
        Discipline,
        verbose_name='discipline',
        related_name='tests'
    )

    questions = models.ManyToManyField(
        Question
    )

    def get_questions(self):
        return ",".join([str(q) for q in self.questions.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'



# ======================
# CodeAnswer
# ======================

class CodeAnswer(models.Model):
    idCodeAnswer = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    question = models.ForeignKey(
        'Question',
        Question,
        verbose_name='question',
        related_name='CodeAnswers'
    )

    inputCode = models.TextField(
        'Input Code',
        max_length=1000
    )

    outputCode = models.TextField(
        'Output Code',
        max_length=1000
    )

    def __str__(self):
        return self.inputCode

    class Meta:
        verbose_name = 'CodeAnswer'
        verbose_name_plural = 'CodeAnswers'

# ======================
# Choice
# ======================

class Choice(models.Model):
    idChoice = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    question = models.ForeignKey(
        'Question',
        Question,
        verbose_name='question',
        related_name='choices'
    )

    correct = models.BooleanField(
        default=False,
    )

    textChoice = models.TextField(
        'Text Choice',
        max_length=100
    )

    def __str__(self):
        return self.textChoice

    class Meta:
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

# ======================
# Answer
# ======================

class Answer(models.Model):
    idAnswer = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    textAnswer = models.TextField(
        'Text Answer',
        max_length=500
    )

    correct = models.BooleanField(
        'correct',
        default=False
    )

    choice = models.ForeignKey(
        'Choice',
        Choice,
        verbose_name='choice',
        related_name='answers'
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='student',
        related_name='answers'
    )

    test = models.ForeignKey(
        'Test',
        Test,
        verbose_name='test',
        related_name='answers'
    )

    question = models.ForeignKey(
        'Question',
        Question,
        verbose_name='question',
        related_name='answers'
    )

    def __str__(self):
        return self.textAnswer

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

# ======================
# Discipline
# ======================

class Discipline(models.Model):
    idDiscipline = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.TextField(
        'Full name',
        max_length=100
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        verbose_name='teacher',
        related_name='disciplines'
    )

    students = models.ManyToManyField(
        Student
    )

    def get_students(self):
        return ",".join([str(s) for s in self.students.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Discipline'
        verbose_name_plural = 'Disciplines'

# ===============================
# TestStudent
# ===============================

class TestStudent(models.Model):
    idTestStudent = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    test = models.ForeignKey(
        'Test',
        Test,
        verbose_name='test',
        related_name='testStudents'
    )

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        verbose_name='student',
        related_name='testStudents'
    )

    scores = models.FloatField(
        'scores',
    )

    timeStart = models.DateTimeField(
        'Time Start'
    )

    timeFinish = models.DateTimeField(
        'Time Finish'
    )

    def __str__(self):
        return self.test

    class Meta:
        verbose_name = 'TestStudent'
        verbose_name_plural = 'TestStudents'
