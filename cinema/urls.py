from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken



from cinema.views import UserView


urlpatterns = [
    
    path("user/",UserView.as_view()),
    path("token/",ObtainAuthToken.as_view()),
]