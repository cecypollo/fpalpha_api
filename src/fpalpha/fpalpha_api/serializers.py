from rest_framework import serializers
#Converts to JSON & validation
 
class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)
