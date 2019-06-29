from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from exams import models

class TeacherTests(APITestCase):
    def test_create_teacher(self):
        """
        Ensure we can create a new teacher object.
        """
        url = reverse('teacher-list')
        data = {'name': 'Fernanda teste', 'email': 'fernanda@test.com', 'dateOfBirth': '01/01/2018', 'gender': 'F'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'Fernanda teste')

