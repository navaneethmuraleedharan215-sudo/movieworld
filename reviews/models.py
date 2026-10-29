from django.db import models
from films.models import movie
from cinema.models import User

# Create your models here.
# from django.db import models
# from django.conf import settings
# from movies.models import Movie

class Review(models.Model):
    movie=models.ForeignKey(movie,on_delete=models.CASCADE,related_name='reviews')

    owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name='reviews')


    msg = models.TextField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5"

    class Meta:
        unique_together = ('movie', 'owner')  

    def __str__(self):
        return f"Review to {self.id}"