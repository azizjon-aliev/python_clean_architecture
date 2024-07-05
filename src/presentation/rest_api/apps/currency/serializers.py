from rest_framework import serializers


class BaseCurrencySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # code = serializers.CharField()
    name = serializers.CharField()
    # symbol = serializers.CharField()


class ListCurrencyResponseSerializer(serializers.Serializer):
    # total = serializers.IntegerField()
    # count = serializers.IntegerField()
    currencies = BaseCurrencySerializer(many=True)


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
