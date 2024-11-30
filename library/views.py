from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author, Book, Borrower
from .forms import AuthorForm, BookForm, BorrowerForm

### HELPER FUNCTIONS ###


def render_partial_or_full(request, template_partial, template_full, context):
    """
    Utility function to render a partial template for HTMX requests
    or the full page for standard requests.
    """
    if request.headers.get('HX-Request'):
        return render(request, template_partial, context)
    return render(request, template_full, context)


def handle_form_submission(request, form, success_trigger):
    """
    Utility function to handle POST form submissions.
    Returns an HTTP response or renders the form with errors.
    """
    if form.is_valid():
        form.save()
        return HttpResponse(status=204, headers={'HX-Trigger': success_trigger})
    return form


def author_list(request):
    """
    Display a list of authors.
    """
    authors = Author.objects.all()
    if request.headers.get('HX-Request'):
        return render(request, 'partials/author_list.html', {'authors': authors})
    return render(request, 'author_list.html', {'authors': authors})


def author_create(request):
    """
    Create a new author and clear the form after submission.
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'refreshPage',  
                    'HX-Trigger-After-Swap': 'clearModal'
                }
            )
    else:
        form = AuthorForm()
    return render(request, 'partials/author_form.html', {'form': form})


def author_update(request, pk):
    """
    Update an existing author and clear the form after submission.
    """
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'refreshPage',  
                    'HX-Trigger-After-Swap': 'clearModal'
                }
            )
    else:
        form = AuthorForm(instance=author)
    return render(request, 'partials/author_form.html', {'form': form, 'author': author})


def author_delete(request, pk):
    """
    Delete an author and clear the modal after submission.
    """
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': 'refreshPage',
                'HX-Trigger-After-Swap': 'clearModal'
            }
        )
    return render(request, 'partials/author_confirm_delete.html', {'author': author})


### BOOK VIEWS ###

def book_list(request):
    """
    Display a list of books.
    """
    books = Book.objects.all()
    return render_partial_or_full(request, 'partials/book_list.html', 'book_list.html', {'books': books})


def book_create(request):
    """
    Create a new book and refresh the book list.
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'refreshPage',
                    'HX-Trigger-After-Swap': 'clearModal'
                }
            )
    else:
        form = BookForm()
    return render(request, 'partials/book_form.html', {'form': form})


def book_update(request, pk):
    """
    Update an existing book and refresh the book list.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'refreshPage',
                    'HX-Trigger-After-Swap': 'clearModal'
                }
            )
    else:
        form = BookForm(instance=book)
    return render(request, 'partials/book_form.html', {'form': form, 'book': book})


def book_delete(request, pk):
    """
    Delete a book and refresh the book list.
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': 'refreshPage',
                'HX-Trigger-After-Swap': 'clearModal'
            }
        )
    return render(request, 'partials/book_confirm_delete.html', {'book': book})


### BORROWER VIEWS ###

def borrower_list(request):
    """
    Display a list of borrowers.
    """
    borrowers = Borrower.objects.all()
    return render_partial_or_full(request, 'partials/borrower_list.html', 'borrower_list.html', {'borrowers': borrowers})


def borrower_create(request):
    """
    Create a new borrower and refresh the borrower list.
    """
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger-After-Swap': 'clearModal',
                    'HX-Trigger': 'refreshPage', 
                }
            )
    else:
        form = BorrowerForm()
    return render(request, 'partials/borrower_form.html', {'form': form})


def borrower_update(request, pk):
    """
    Update an existing borrower and refresh the borrower list.
    """
    borrower = get_object_or_404(Borrower, pk=pk)
    if request.method == 'POST':
        form = BorrowerForm(request.POST, instance=borrower)
        if form.is_valid():
            form.save()
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': 'refreshPage',
                    'HX-Trigger-After-Swap': 'clearModal'
                }
            )
    else:
        form = BorrowerForm(instance=borrower)
    return render(request, 'partials/borrower_form.html', {'form': form, 'borrower': borrower})


def borrower_delete(request, pk):
    """
    Delete a borrower and refresh the borrower list.
    """
    borrower = get_object_or_404(Borrower, pk=pk)
    if request.method == 'POST':
        borrower.delete()
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': 'refreshPage',
                'HX-Trigger-After-Swap': 'clearModal'
            }
        )
    return render(request, 'partials/borrower_confirm_delete.html', {'borrower': borrower})
