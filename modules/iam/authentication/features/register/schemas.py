from rest_framework import serializers

# Serializer for user registration request
# This serializer is used to validate the data sent in the registration request. It ensures that the required fields are present and meet the specified criteria (e.g., email format, password length).

class RegisterRequestSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True, min_length=8)