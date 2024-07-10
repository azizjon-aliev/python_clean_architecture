from rest_framework import serializers


class BaseCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class ListCurrencyResponseSerializer(BaseCurrencySerializer):
    pass


class DetailCurrencyResponseSerializer(BaseCurrencySerializer):
    code = serializers.CharField()
    symbol = serializers.CharField()


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
