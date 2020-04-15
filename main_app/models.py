from django.db import models
from django.urls import reverse

class Producer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Song(models.Model): 
    name = models.TextField(max_length=250)
    genre = models.TextField(max_length=250)
    album = models.TextField(max_length=250)
    artist = models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwags={'song_id': self.id})

