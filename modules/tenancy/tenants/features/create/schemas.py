from rest_framework import serializers


class CreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)
    primary_domain = serializers.CharField(max_length=255)

    description = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    logo = serializers.URLField(
        required=False,
        allow_blank=True,
    )


class CreateResponseSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    name = serializers.CharField()
    slug = serializers.CharField()
    primary_domain = serializers.CharField()