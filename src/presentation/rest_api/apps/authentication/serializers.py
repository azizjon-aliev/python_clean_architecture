from django.contrib.auth import authenticate
from rest_framework import serializers

from src.domain.entities.account import User
from src.infrastructure.repositories.account_repository import UserRepository

from src.interactor.errors.error_classes import InvalidCredentials
from src.interactor.interfaces.providers.token_provider import TokenProviderInterface
from src.presentation.rest_api.config.containers import container

class RegisterStep1RequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    def validate_email(self, value: str) -> str:
        if value and UserRepository().exists(email=value):
            raise serializers.ValidationError("Such email is already in use.")
        return value

    def validate_username(self, value: str) -> str:
        if value and UserRepository().exists(username=value):
            raise serializers.ValidationError("Such username is already in use.")
        return value

    def validate_password(self, value: str) -> str:
        if not User.check_password(password=value):
            raise serializers.ValidationError("Incorrect password format.")
        return value

    def validate(self, data: dict):
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        if password and password != password_confirmation:
            raise serializers.ValidationError("The passwords don't match")
        return data



class LoginRequestSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError({"detail": "Invalid username or password"})

        return attrs


class RefreshTokenRequestSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()

    def validate_refresh_token(self, value: str) -> str:
        token_provider = container.resolve(TokenProviderInterface)
        try:
            token_provider.verify_refresh_token(value)
        except InvalidCredentials as e:
            raise serializers.ValidationError(str(e))
        return value


class TokenResponseSerializer(serializers.Serializer):
    access_token = serializers.CharField()
    refresh_token = serializers.CharField()

