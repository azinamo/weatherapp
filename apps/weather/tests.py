from django.test import TestCase

from .views import Forecast

# Create your tests here.
class LandingPageTest(TestCase):

    def test_root_url_resolves_to_home(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
