from tools.models import Tool, Type
from rest_framework import serializers


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ["code", 'type', 'tags', 'quantity', 'active', 'current_user', 'current_location', 'date_updated']


class ToolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name']