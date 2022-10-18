from operator import itemgetter

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from api.paginations import OrderSetPagination
from manual.models import Color, CarBrand, CarModel
from manual.serlializers import ColorSerializer, CarBrandSerializer, CarModelSerializer, CountOrderBrandsSerializer, \
    CarModelListSerializer
from orders.models import Order
from orders.serlializers import OrderSerializer, CountOrderColorsSerializer, OrderListSerializer


class ColorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer


class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    pagination_class = OrderSetPagination


class CarBrandDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer


class CarBrandListView(generics.ListAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    pagination_class = OrderSetPagination


class CarModelDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarModelListView(generics.ListAPIView):
    # queryset = CarModel.objects.all()
    serializer_class = CarModelListSerializer
    pagination_class = OrderSetPagination

    def get_queryset(self):
        all_models = []
        for model in CarModel.objects.all():
            all_models.append({'id': model.pk, 'name': model.name, 'brand': model.brand.name})
        return all_models

class OrderDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    # queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    pagination_class = OrderSetPagination

    def get_queryset(self):
        all_orders = []

        if 'sorted' in self.kwargs:
            sort_sign = 'count' if self.kwargs['sorted'] == 'increase' else '-count'
        else:
            sort_sign = '-count'

        for order in Order.objects.all().order_by(sort_sign):
            all_orders.append({
                'id': order.pk,
                'model': order.model.name,
                'brand': order.model.brand.name,
                'color': order.color.hex,
                'count': order.count,
                'date': order.date
            })

        return all_orders


class OrderFilterListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    pagination_class = OrderSetPagination

    def get_queryset(self):
        brand = self.kwargs['brand']
        need_orders = []

        for one in CarBrand.objects.filter(name=brand):
            order = Order.objects.get(pk=one.id)
            need_orders.append({
                'id': order.pk,
                'model': order.model.name,
                'brand': order.model.brand.name,
                'color': order.color.hex,
                'count': order.count,
                'date': order.date
            })

        return need_orders


class CountOrderColorsListView(generics.ListAPIView):
    serializer_class = CountOrderColorsSerializer
    pagination_class = OrderSetPagination

    def get_queryset(self):
        color_list = {}
        for order in Order.objects.all():
            if order.color.hex in color_list:
                color_list[order.color.hex] += order.count
            else:
                color_list[order.color.hex] = order.count

        need_orders = []
        [need_orders.append({'color': key, 'count': val}) for key, val in color_list.items()]

        return need_orders


class CountOrderBrandsListView(generics.ListAPIView):
    serializer_class = CountOrderBrandsSerializer
    pagination_class = OrderSetPagination

    def get_queryset(self):
        brand_list = {}
        for order in Order.objects.all():
            if order.model.brand.name in list(brand_list):
                brand_list[order.model.brand.name] += order.count
            else:
                brand_list[order.model.brand.name] = order.count

        need_orders = []
        [need_orders.append({'brand': key, 'count': val}) for key, val in brand_list.items()]

        return need_orders

