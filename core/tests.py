from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from exams import models as core

class TeacherTests(APITestCase):
    def test_create_teacher(self):
        """
        Ensure we can create a new teacher object.
        """
        url = reverse('core-api:api-teacher-list')
        data = {'name': 'Fernanda teste', 'email': 'fernanda@test.com', 'dateOfBirth': '2018-01-01', 'gender': 'F', 'username': 'userteste1', 'password': 'nanda1.io'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(core.Teacher.objects.count(), 1)
        # self.assertEqual(core.Teacher.objects.get().name, 'Fernanda teste')

