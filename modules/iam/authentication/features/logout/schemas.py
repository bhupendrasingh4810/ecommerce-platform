from rest_framework import serializers


class LogoutRequestSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()