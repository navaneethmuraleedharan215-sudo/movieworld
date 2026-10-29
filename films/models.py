
from django.db import models

from cinema.models import User

# Create your models here.

class movie(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    release_date = models.DateField()

    LANGUAGE_CHOICES = [
        ('English', 'English'),
        ('Malayalam', 'Malayalam'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('Telugu', 'Telugu'),
        ('Kannada', 'Kannada'),
    ]

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES,default="Malayalam")

    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('horror', 'Horror'),
        ('sci_fi', 'Science Fiction'),
    ]


    genre = models.CharField(max_length=100,choices=GENRE_CHOICES,default="drama")

    director = models.CharField(max_length=150)

    cast = models.TextField()
        
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at =models.DateField(auto_now=True)

    created_by =models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"