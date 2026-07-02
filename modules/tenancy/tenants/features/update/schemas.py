from rest_framework import serializers


class CreateTenantRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)
    primary_domain = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    currency = serializers.CharField(default="USD")
    timezone = serializers.CharField(default="UTC")