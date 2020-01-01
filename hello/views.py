from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting, Quote


def index(request):
    quotes = Quote.objects.all()
    quote = quotes[0]
    print("quote_is", quote)
    return render(request, "index.html", {"quote": quote})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
