from django.db import models

# Create your models here.
class Song(models.Model): 
    name = models.TextField(max_length=250)
    genre = models.TextField(max_length=250)
    album = models.TextField(max_length=250)
    artist = models.TextField(max_length=250)