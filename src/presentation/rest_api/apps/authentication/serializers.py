from rest_framework import serializers


class RegisterRequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)


class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class RefreshTokenRequestSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()


class TokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()
