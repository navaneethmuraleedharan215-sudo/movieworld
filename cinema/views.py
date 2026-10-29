from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from cinema.serializers import UserSerializer
from cinema.models import User

# Create your views here.
class UserView(APIView):

    def post (self,request):

        form_data = request.data

        serializer_inst = UserSerializer(data=form_data)

        if serializer_inst.is_valid():

            cleaned_data = serializer_inst.validated_data

            instance = User.objects.create_user(role="user",**cleaned_data)

            serializer_inst = UserSerializer(instance)

            return Response(data=serializer_inst.data)

        else:

            return Response(data=serializer_inst.errors)
