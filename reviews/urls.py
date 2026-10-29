from django.urls import path
from reviews.views import ReviewCreateView,ReviewRetriveApiView

urlpatterns=[
    path('opinion/<int:pk>/review/',ReviewCreateView.as_view()),
    path('opinion/<int:pk>/',ReviewRetriveApiView.as_view()),

    
]