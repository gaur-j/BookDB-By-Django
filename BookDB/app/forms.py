from django import forms
from .models import Book  # Ensure your model is correctly imported

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'price']  # List all fields you want in the form
fields = '__all__'
