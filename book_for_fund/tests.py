from django.test import TestCase
from rest_framework.test import APIClient 
from rest_framework import status 
from user.models import MyCustomUser 
from .models import BookForFund 
# Create your tests here.

class BookForFundTests(TestCase):
    def setUp(self):
        self.client = APIClient() 

        self.user  = MyCustomUser.objects.create_user(
        first_name = 'goru',
        last_name  = 'dalal',  
        email      = 'gorudalal@gmail.com',
        password   = 'password123',
        phone      = '01712345678',
    )
        
    def test_get_all_books(self):
        res = self.client.get('/book-for-fund/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
    def test_create_book(self):
        self.client.force_authenticate(user=self.user)
        res = self.client.post('/book-for-fund/', {
            "book_name" : 'goru',
            "author_name"  : 'dalal',
            "donation" : 100,
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_single_book(self):
        book = BookForFund.objects.create(
            donor       = self.user,
            book_name   = 'Test Book',
            author_name = 'Test Author',
            donation    = 100,
        )
        res = self.client.get(f'/book-for-fund/{book.slug}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)



    