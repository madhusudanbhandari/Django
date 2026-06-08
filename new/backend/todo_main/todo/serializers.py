from rest_framework import serializers
from .models import my_user,todo
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=my_user
        fields='__all__'

    def create(self,validated_data):
        password=validated_data.pop('password')

        user=my_user.objects.create_user(**validated_data )
        user.set_password(password)
        user.save()
        return user
    

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo
        fields='__all__'
        read_only_fields=['user']