from django.db import models

# Create your models here.

from films.models import movie

from cinema.models import User

# Create your models here.

class song(models.Model):

    LANGUAGE_CHOICES = [
        ('Malayalam', 'Malayalam'),
        ('Tamil', 'Tamil'),
        ('Hindi', 'Hindi'),
        ('English', 'English'),
        ('Telugu', 'Telugu'),
    ]

    GENRE_CHOICES = [
        ('Melody', 'Melody'),
        ('Romantic', 'Romantic'),
        ('Sad', 'Sad'),
        ('Devotional', 'Devotional'),
        ('Rock', 'Rock'),
        ('Pop', 'Pop'),
        ('Classical', 'Classical'),
    ]

    title = models.CharField(max_length=200)

    album = models.CharField(max_length=200)

    singer = models.CharField(max_length=150)

    music_director = models.CharField(max_length=150)

    language = models.CharField(
        max_length=50,
        choices=LANGUAGE_CHOICES,default="Malayalam"
    )

    genre = models.CharField(
        max_length=100,
        choices=GENRE_CHOICES,default="Melody"
    )

    release_date = models.DateField()

    duration = models.PositiveIntegerField()

    lyrics = models.TextField()

    track_number =models.PositiveBigIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    movie = models.ForeignKey(movie,on_delete=models.CASCADE)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):

        last_object =song.objects.filter(movie=self.movie).last()

        if last_object:

            self.track_number =last_object.track_number =+1

        else:

            self.track_number =1


        return super().save( *args,**kwargs)
