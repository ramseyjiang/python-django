from django.test import TestCase
from web.forms import BookForm
from datetime import date

class BookFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'title': "Valid Book",
            'author': 1,  # Assuming the Author with ID 1 exists
            'publisher': 1,  # Assuming the Publisher with ID 1 exists
            'price': 19.99,
            'publication_date': date.today(),
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'title': "",  # Title is required
            'price': "invalid_price",  # Should be a float
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())