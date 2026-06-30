from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.
class test_homepage(TestCase):

    def TestHomePage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
