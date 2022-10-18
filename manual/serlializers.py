from rest_framework import serializers
from .models import Color, CarBrand, CarModel


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class CarModelListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    brand = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)


class CountOrderBrandsSerializer(serializers.Serializer):
    brand = serializers.CharField(max_length=200)
    count = serializers.IntegerField()
