from django.http import HttpResponse
from web.models import Person

def hello(request):
    person = Person.objects.first()
    return HttpResponse(f"Hello, {person}!")