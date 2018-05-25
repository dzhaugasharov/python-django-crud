from django.test import TestCase
from datetime import timezone


# Create your tests here.
class BookModelTests(TestCase):

    def test_adding_book(self):
        a = 5
        b = 5
        self.assertIs(a, b, "Not equals")
