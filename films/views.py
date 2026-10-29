
from django.shortcuts import render

from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView

from rest_framework import authentication,permissions
from rest_framework.response import Response

from films.serializers import MovieSerializer
from films.models import movie
from films.permissions import IsOwner


# Create your views here.

class MovieListView(ListAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]

    serializer_class =MovieSerializer

    queryset =movie.objects.all()

class MovieCreateView(CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):

        form_data =request.data

        serializer_inst = MovieSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data =serializer_inst.validated_data

            serializer_inst.save(created_by=request.user)

            return Response (data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)

class MovieRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    serializer_class =MovieSerializer

    queryset = movie.objects.all()


