from rest_framework import serializers


class NotFoundResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(default="Страница не найдена.")
