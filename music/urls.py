from django.urls import path

from music.views import SongCreateView
from music.views import SongRetrieveUpdateDeleteView


urlpatterns = [
    path("song/<int:pk>/",SongCreateView.as_view()),

    path("<int:pk>/songs/",SongRetrieveUpdateDeleteView.as_view()),


]