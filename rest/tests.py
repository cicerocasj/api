from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase


class ClientTests(TestCase):

    def get_token(self):
        response = self.client.post('/api-token-auth/', {'username': self.username, 'password': self.password})
        return response.json().get('token')

    def setUp(self):
        self.client = APIClient()
        self.username = 'cicero'
        self.password = 'brasilprev'
        self.user = User.objects.create_superuser(self.username, 'cicero@brasilprev.com', self.password)
        self.token = self.get_token()
        self.assertIsInstance(self.token, str)

    def test_get_client(self):
        response = self.client.get('/v1/client/')
        self.assertEqual(response.status_code, 401, 'Verify error for Authentication credentials')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.get('/v1/client/')
        self.assertEqual(response.status_code, 200, 'Verify success for Authentication credentials')
        data = response.json()
        self.assertIsInstance(data, list, 'Check if response is a list')
        empty_list = []
        self.assertCountEqual(data, empty_list, 'Check if list is empty')

    def test_post_client(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        new_client = {'name': 'Cicero', 'cpf': '12345', 'birth': '1990-09-30 04:10'}
        response = self.client.post('/v1/client/', new_client)
        self.assertEqual(response.status_code, 201, 'Verify success post for create client')
        data = response.json()
        self.assertIsInstance(data, dict, 'Check if response is a dict')
        response = self.client.get('/v1/client/')
        data = response.json()
        self.assertEquals(len(data), 1, 'Check if list one element')