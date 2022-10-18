from django.contrib import admin
from .models import CarBrand, CarModel, Color

# Register your models here.
admin.site.register(Color)
admin.site.register(CarBrand)
admin.site.register(CarModel)
