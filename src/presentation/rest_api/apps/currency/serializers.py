from rest_framework import serializers


class ListCurrencyResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()


class DetailCurrencyResponseSerializer(ListCurrencyResponseSerializer):
    code = serializers.CharField()
    symbol = serializers.CharField()


class CreateCurrencyRequestSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()


class UpdateCurrencyRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, default=None)
    name = serializers.CharField(required=False, default=None)
    symbol = serializers.CharField(required=False, default=None)
