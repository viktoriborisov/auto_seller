from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderListSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=200)
    brand = serializers.CharField(max_length=200)
    color = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
    date = serializers.DateTimeField()


class CountOrderColorsSerializer(serializers.Serializer):
    color = serializers.CharField(max_length=200)
    count = serializers.IntegerField()

