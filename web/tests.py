from django.test import TestCase, Client
from django.urls import reverse
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

#Test all CRUD operations for Book, Author, and Publisher.
class BookViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name="Test Author")
        self.publisher = Publisher.objects.create(name="Test Publisher")
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publisher=self.publisher,
            price=19.99,
            publication_date=date.today(),
        )

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")

    def test_book_create_view(self):
        response = self.client.post(reverse('book_create'), {
            'title': "New Book",
            'author': self.author.id,
            'publisher': self.publisher.id,
            'price': 25.00,
            'publication_date': "2024-01-01",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Book.objects.count(), 3)

    def test_book_update_view(self):
        response = self.client.post(reverse('book_update', args=[self.book.id]), {
            'title': "Updated Book",
            'author': self.author.id,
            'publisher': self.publisher.id,
            'price': 29.99,
            'publication_date': "2024-01-02",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_book_delete_view(self):
        response = self.client.post(reverse('book_delete', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Book.objects.count(), 1)

class AuthorViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.author = Author.objects.create(name="Test Author")

    def test_author_list_view(self):
        response = self.client.get(reverse('author_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Author")

    def test_author_create_view(self):
        response = self.client.post(reverse('author_create'), {
            'name': "New Author",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Author.objects.count(), 3)

    def test_author_update_view(self):
        response = self.client.post(reverse('author_update', args=[self.author.id]), {
            'name': "Updated Author",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, "Updated Author")

    def test_author_delete_view(self):
        response = self.client.post(reverse('author_delete', args=[self.author.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Author.objects.count(), 1)

class PublisherViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.publisher = Publisher.objects.create(name="Test Publisher")

    def test_publisher_list_view(self):
        response = self.client.get(reverse('publisher_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Publisher")

    def test_publisher_create_view(self):
        response = self.client.post(reverse('publisher_create'), {
            'name': "New Publisher",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Publisher.objects.count(), 3)

    def test_publisher_update_view(self):
        response = self.client.post(reverse('publisher_update', args=[self.publisher.id]), {
            'name': "Updated Publisher",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.publisher.refresh_from_db()
        self.assertEqual(self.publisher.name, "Updated Publisher")

    def test_publisher_delete_view(self):
        response = self.client.post(reverse('publisher_delete', args=[self.publisher.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after success
        self.assertEqual(Publisher.objects.count(), 1)