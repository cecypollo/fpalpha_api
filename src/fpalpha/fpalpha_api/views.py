from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from . import serializers
from . import models
from . import permissions

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

class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class=serializers.HelloSerializer

    def list(self, request): #returns a hello message
        a_viewset=[
            'User actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hey {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    #Creating and updating profiles
    serializer_class=serializers.UserProfileSerializer #Knows the model because it is set in Serializers
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)      #You can add more auth classes
    permission_classes=(permissions.UpdateOwnProfile,)
