from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers, status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from authapiapp.models import user
from authapiapp.serializers import userSerializer


#This is plural user
class TestAPIVIew(APIView):

    def get(self, request, format=None):
        return Response({'name': 'Hii welcome to this website'})

#Get method 
class CheckListsAPIView(APIView):
    serializer_class = userSerializer

    def get(self, request, format=None):
        data = user.objects.all()
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data, status=status.HTTP_200_OK)


#Post method 
    def post(self, request, format=None):
        print(request.data)  #request.data will create form 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#singular user 
# This class will give the single record with help of primary key when you will going to search for record 
class CheckListAPIView(APIView):
    serializer_class = userSerializer
    # try will check the id if id is present it will retrurn data and except will give http404 error if id will not present 

    def get_object(self, pk):
        try:
            return user.objects.get(pk=pk)
        except user.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        print(serialized_data)

        return Response(serialized_data, status=status.HTTP_200_OK)


#then put method 
    def put(self, request, pk, format=None):
        checklist = self.get_object(pk)
        serializer = self.serializer_class(checklist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Delete method 
    def delete(self, request, pk, format=None):
        checklist = self.get_object(pk)
        checklist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

