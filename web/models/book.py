from django.db import models
from .author import Author
from .publisher import Publisher

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publication_date = models.DateField()

    def __str__(self):
        return self.title