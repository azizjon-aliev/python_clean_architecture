from rest_framework import serializers


class CreateCurrencyRequestSerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()


class CreateCurrencyResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()


class UpdateCurrencyRequestSerializer(serializers.Serializer):
    code = serializers.CharField(required=False, default=None)
    name = serializers.CharField(required=False, default=None)
    symbol = serializers.CharField(required=False, default=None)


class UpdateCurrencyResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    code = serializers.CharField()
    name = serializers.CharField()
    symbol = serializers.CharField()
