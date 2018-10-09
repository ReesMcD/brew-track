from django.test import TestCase, Client
from bar.models import Bar

# Create your tests here.
class Bar_Pages_Test(TestCase):
    # def setUp(self):
    #     Bar.objects.create(name="Test Bar")

    def test_bar_home(self):
        print("Testing for bar...")
        response = self.client.get('/bar/', follow=True)
        self.assertEqual(response.status_code, 200)
