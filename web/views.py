from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db import connection
from .models import Person, Book, Author, Publisher
from .forms import BookForm, AuthorForm, PublisherForm

def home(request):
    return render(request, 'web/home.html')

def hello(request):
    person = Person.objects.first()
    return HttpResponse(f"Hello, {person}!")

def health_check(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")  # Simple query to check DB connectivity
        return JsonResponse({'status': 'healthy'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

# Book Views
def book_list(request):
    books = Book.objects.all()

    if not books.exists():  # Check if the queryset is empty
        exist = "No books available. Please add some books!"
        return render(request, 'web/books/list.html', {'exist': exist})
    return render(request, 'web/books/list.html', {'books': books})

def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'web/books/form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'web/books/form.html', {'form': form})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, 'web/books/confirm_delete.html', {'book': book})

# Author Views
def author_list(request):
    authors = Author.objects.all()
    if not authors.exists():  # Check if the queryset is empty
        exist = "No authors available. Please add some authors!"
        return render(request, 'web/authors/list.html', {'exist': exist})
    return render(request, 'web/authors/list.html', {'authors': authors})

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'web/authors/form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'web/authors/form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect('author_list')
    return render(request, 'web/authors/confirm_delete.html', {'author': author})


# Publisher Views
def publisher_list(request):
    publishers = Publisher.objects.all()
    if not publishers.exists():  # Check if the queryset is empty
        exist = "No publishers available. Please add some publishers!"
        return render(request, 'web/publishers/list.html', {'exist': exist})
    return render(request, 'web/publishers/list.html', {'publishers': publishers})

def publisher_create(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm()
    return render(request, 'web/publishers/form.html', {'form': form})

def publisher_update(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect('publisher_list')
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'web/publishers/form.html', {'form': form})

def publisher_delete(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == "POST":
        publisher.delete()
        return redirect('publisher_list')
    return render(request, 'web/publishers/confirm_delete.html', {'publisher': publisher})