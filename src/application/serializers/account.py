from rest_framework import serializers
from src.domain.entities.account import User


class BaseCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()


class RegisterStep1RequestSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=13)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)
    password_confirmation = serializers.CharField(min_length=8)

    def validate_phone(self, value: str) -> str:
        if not User.check_phone_number(phone=value):
            raise serializers.ValidationError("Неверный формат номер телефона.")
        return value

    def validate_password(self, value: str) -> str:
        if not User.check_password(password=value):
            raise serializers.ValidationError("Неверный формат пароля.")
        return value

    def validate(self, data):
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        if password and password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")
        return data


class CreateCurrencyRequestSerializer(BaseCurrencySerializer):
    pass


class CreateCurrencyResponseSerializer(BaseCurrencySerializer):
    pass


class UpdateCurrencyRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, default=None)
    name = serializers.CharField(required=False, default=None)
    symbol = serializers.CharField(required=False, default=None)


class UpdateCurrencyResponseSerializer(BaseCurrencySerializer):
    pass


class DetailCurrencyResponseSerializer(BaseCurrencySerializer):
    pass
