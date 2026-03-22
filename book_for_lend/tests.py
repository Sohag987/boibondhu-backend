from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user.models import MyCustomUser 
from .models import BookForLend 

# Create your tests here.


class BookForLendTests(TestCase):
    def setUp(self):  
        self.client = APIClient()
        self.user = MyCustomUser.objects.create_user(
            first_name = 'goru',
            last_name  = 'dalal',
            email      = 'gorudalal@gmail.com',
            password   = 'password123',
            phone      = '01712345678'
        )

    def test_get_all_books(self):  
        res = self.client.get('/book-for-lend/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_book(self):  
        self.client.force_authenticate(user=self.user)
        res = self.client.post('/book-for-lend/', {
            'book_name'  : 'The Great Gatsby',
            'author_name': 'F. Scott Fitzgerald',
            'description': 'A novel set in the Roaring Twenties.',
            'rent_price' : 2.99,
        })
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_single_book(self):
        book = BookForLend.objects.create(
            lender      = self.user,
            book_name   = 'Test Book',
            author_name = 'Test Author',
            duration    = 30,
            
            
        )
        res = self.client.get(f'/book-for-lend/{book.slug}/')
        self.assertEqual(res.status_code, status.HTTP_200_OK)