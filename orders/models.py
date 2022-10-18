import datetime

from django.core.validators import MinValueValidator
from django.db import models
from manual.models import CarBrand, CarModel, Color


# Create your models here.
class Order(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    count = models.IntegerField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(default=datetime.datetime.now())
