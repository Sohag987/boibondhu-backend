from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import MyCustomUser

# Create your tests here.

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient() 

    def test_user_registration(self):
        res = self.client.post('/register/', {
            'first_name': 'malu',
            'last_name': 'dalal',
            'email': 'maludalal@gmail.com',
            'password':'password123',
            'phone': '01712345678'})
        self.assertEqual(res.status_code,status.HTTP_201_CREATED)

  

class UserLogintests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = MyCustomUser.objects.create_user(
            first_name='goru',
            last_name='dalal',
            email = 'gorudalal@gmail.com',
            password = 'password123',
            phone='01712345678'

        )
    def test_user_login_invaid(self):
         res = self.client.post('/login/', {
            'email': 'maludalal@gmail.com',
            'password':'wrongword123',})
         
         self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)



    def test_log_in_valid(self):
        res = self.client.post('/login/', {
            'email': 'gorudalal@gmail.com',
            'password': 'password123'
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('access', res.data)
        self.assertIn('refresh', res.data)
 