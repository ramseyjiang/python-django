from django.test import TestCase
from web.models import Author, Publisher, Book
from datetime import date

#Ensure models correctly create and save data.
class AuthorModelTest(TestCase):
    def test_author_creation(self):
        author = Author.objects.create(name="Test Author")
        self.assertEqual(author.name, "Test Author")

class PublisherModelTest(TestCase):
    def test_publisher_creation(self):
        publisher = Publisher.objects.create(name="Test Publisher")
        self.assertEqual(publisher.name, "Test Publisher")

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name="Test Author")
        self.publisher = Publisher.objects.create(name="Test Publisher")

    def test_book_creation(self):
        book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publisher=self.publisher,
            price=19.99,
            publication_date=date.today(),
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(book.price, 19.99)
        self.assertEqual(book.author.name, "Test Author")
        self.assertEqual(book.publisher.name, "Test Publisher")