from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response
from films.models import movie

# Create your views here.

class ReviewCreateView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,pk=None):

        movie_id=pk
        movie_object=get_object_or_404(movie,id=movie_id)
        form_data=request.data
        serializer_instance=ReviewSerializer(data=form_data)
        if serializer_instance.is_valid():
            instance=serializer_instance.save(movie=movie_object,owner=request.user)
            serializer_instance=ReviewSerializer(instance)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)


    

class ReviewRetriveApiView(APIView):

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    # serializer_class=SubmissionSerializer
    # queryset=Submission.objects.all()

    def get(self,request,pk=None):
        review_id=pk
        instance=get_object_or_404(Review,id=pk)
        serializer_instance=ReviewSerializer(instance)
        return Response(data=serializer_instance.data)

