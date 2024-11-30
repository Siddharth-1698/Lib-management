from django import forms
from .models import Author, Book, Borrower

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'published_date']

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ['name', 'book', 'return_date']
