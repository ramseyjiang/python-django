from django import forms
from web.models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']