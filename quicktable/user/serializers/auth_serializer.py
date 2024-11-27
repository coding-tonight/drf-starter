from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

from user.models import QTUser

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
    
    
    def validate_email(self, value):
        if not QTUser.objects.filter(email=value).exists():
            return serializers.ValidationError("User does not exists")
        return value

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        
        if user := authenticate(email=email, password=password):
            return user
        
        raise AuthenticationFailed()