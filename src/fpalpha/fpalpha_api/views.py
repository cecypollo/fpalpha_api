from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

#Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        an_apiview=[
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Similar to a traditional Django view',
            'Gives you the most control over you logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        serializer=serializers.HelloSerializer(data=request.data) #Creates a serializer object
        #Data validation
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            #Serializer errors returns ALL the errors, then specify bad request one
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):    #For updating
        return Response({'method':'put'})

    def patch(self, request, pk=None):  #Updates specific fields
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        return Response({'method':'delete'})
