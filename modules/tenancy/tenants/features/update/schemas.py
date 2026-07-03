from rest_framework import serializers


class UpdateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)
    primary_domain = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    logo = serializers.URLField(required=False, allow_blank=True)
    currency = serializers.CharField(max_length=3)
    timezone = serializers.CharField(max_length=100)
    status = serializers.CharField()
    is_active = serializers.BooleanField()


class UpdateResponseSerializer(serializers.Serializer):
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