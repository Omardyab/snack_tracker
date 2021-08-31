from django.test import TestCase
from django.urls import reverse 
#   Create your tests here.

class SnackTests(TestCase):
    def test_snacks_list(self):

        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    def test_snacks_list_template(self):
        url = reverse('snacks_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snacks_list.html')
        self.assertTemplateUsed(response, 'base.html')