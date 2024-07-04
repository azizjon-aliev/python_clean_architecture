from rest_framework import serializers
from src.domain.entities.account import User
from src.infrastructure.repositories.account_repository import UserRepository


class BaseCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()


class RegisterStep1RequestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    def validate_email(self, value: str) -> str:
        if value and UserRepository().exists(email=value):
            raise serializers.ValidationError("Such email is already in use.")
        return value

    def validate_password(self, value: str) -> str:
        if not User.check_password(password=value):
            raise serializers.ValidationError("Incorrect password format.")
        return value

    def validate(self, data):
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        if password and password != password_confirmation:
            raise serializers.ValidationError("The passwords don't match")
        return data


class RegisterStep1ResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()
    email = serializers.EmailField()
