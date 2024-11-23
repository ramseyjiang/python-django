from django.shortcuts import render, get_object_or_404, redirect
from web.models import Author
from web.forms import AuthorForm

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