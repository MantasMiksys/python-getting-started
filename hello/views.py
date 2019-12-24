from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Quote

# Create your views here.
def index(request):

    return render(request, "index.html")

def quotes(request):
    quotes = Quote.objects.all()
    print("quotes are", quotes)
    return render(request, "index.html", {"quotes": quotes})

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
