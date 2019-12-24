from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Quote(models.Model) :
    created = models.DateTimeField("date created", auto_now_add=True)
    quote = models.TextField("quote")
    author = models.TextField("author")