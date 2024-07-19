from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book

class TestHomePage(SimpleTestCase):
    def test_status(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('home')
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'home.html')



class TestBookListPage(TestCase):
    def test_status(self):
        url = reverse('book_list') 
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_template_used(self):
        url = reverse('book_list') 
        res = self.client.get(url)
        self.assertTemplateUsed(res, 'list_of_books.html')
