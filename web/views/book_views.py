from django.shortcuts import render, redirect, get_object_or_404
from web.models import Book
from web.forms import BookForm

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