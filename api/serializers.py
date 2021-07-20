from tools.models import Tool, Type
from rest_framework import serializers
from accounts.models import User
from rest_framework.validators import UniqueTogetherValidator


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'pk',
            'location',
        )
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username', 'email']
            )
        ]


class ToolSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tool
        fields = ["code", 'type', 'tags', 'quantity', 'active', 'current_user', 'current_location']


class ToolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ["pk", 'name']


