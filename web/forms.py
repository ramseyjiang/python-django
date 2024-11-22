from django import forms
from .models import Book, Author, Publisher

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'price', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={
                'placeholder': 'YYYY-MM-DD',  # Example format
                'type': 'date'  # Makes it a date picker in modern browsers
            }),
        }

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']