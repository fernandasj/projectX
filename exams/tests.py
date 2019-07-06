from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.test import APIClient 

from exams import models as exams
from core import models as core

class TestCreateTests(TestCase):
    """
        Ensure we can create a new Test object.
    """

    def test_create_test(self):

        user1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        user2 = User.objects.create_user('mari', 'mari@thebeatles.com', 'maripassword')

        teacher = core.Teacher.objects.create(
            name='Professor teste', 
            email='professor@test.com', 
            dateOfBirth='2018-01-01', 
            gender='M', 
            user=user1
        )

        student = core.Student.objects.create(
            name='Aluno teste', 
            email='aluno@test.com', 
            dateOfBirth='2018-01-01', 
            gender='M',
            course='ADS',
            user=user2          
        )

        discipline = exams.Discipline.objects.create(
            name='Disciplina teste', 
            teacher=teacher,
        )
        discipline.students.add(student)

        question = exams.Question.objects.create(
            headQuestion='Questão Teste',
            typeQuestion='Code',
            discipline=discipline
        )

        codeAnswer = exams.CodeAnswer.objects.create(
            question=question,
            inputCode='1 2',
            outputCode='3'
        )
       
        url = reverse('exams-api:api-test-list')
        headers = {'Authorization': 'Token de2fa67c6fa3a9eb8277801293fac01d4717fca2'}
        data = {'aplicationDate': '2019-07-06 18:39:56', 'aplicationDateLimit': '2019-07-06 19:39:56', 'name': 'Avaliação teste', 'discipline': str(discipline.pk), 'questions': str(question.pk)}
        
        response = self.client.post(url, data, format='json', headers=headers)     
        
        print(teacher)
        print(student)
        print(discipline)
        print(question)
        print(codeAnswer)
        print(response.data)
        print(response.status_code)    

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        

