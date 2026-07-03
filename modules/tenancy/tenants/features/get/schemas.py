from rest_framework import serializers


class GetResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    slug = serializers.CharField()
    primary_domain = serializers.CharField()
    description = serializers.CharField()
    logo = serializers.URLField(allow_blank=True)
    currency = serializers.CharField()
    timezone = serializers.CharField()
    status = serializers.CharField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()