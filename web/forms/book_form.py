from django import forms
from web.models import Book

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