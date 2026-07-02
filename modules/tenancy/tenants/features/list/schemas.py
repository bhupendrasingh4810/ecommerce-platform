from rest_framework import serializers


class TenantSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    slug = serializers.CharField()
    primary_domain = serializers.CharField()
    currency = serializers.CharField()
    timezone = serializers.CharField()
    status = serializers.CharField()