from django.db import models
from colorfield.fields import ColorField


# Create your models here.
class Color(models.Model):
    hex = ColorField(max_length=200)


class CarBrand(models.Model):
    name = models.CharField(max_length=200)


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)





