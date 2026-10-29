
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from music.serializers import SongSerializer
from films.models import movie
from music.models import song

# Create your views here.


class SongCreateView(CreateAPIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]


    def post(self,request,pk=None):

        movie_id =pk

        movie_object =movie.objects.get(id=movie_id)

        form_data = request.data

        serializer_inst = SongSerializer(data=form_data)

        if serializer_inst.is_valid():

            serializer_inst.save(movie=movie_object,created_by=request.user)

            return Response (data=serializer_inst.data)

        else:

            return Response (data=serializer_inst.errors)


class SongRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes =[permissions.IsAuthenticated]

    serializer_class =SongSerializer

    queryset =song.objects.all()