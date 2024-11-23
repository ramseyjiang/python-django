from django.shortcuts import render, get_object_or_404, redirect
from web.models import Publisher
from web.forms import PublisherForm

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