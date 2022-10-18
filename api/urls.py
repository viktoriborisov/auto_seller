from django.urls import path
from api import views

urlpatterns = [
    path('color/<int:pk>', views.ColorDetailView.as_view(), name='color_detail_view'),
    path('colors/', views.ColorListView.as_view(), name='color_list_view'),

    path('brand/<int:pk>', views.CarBrandDetailView.as_view(), name='car_brand_detail_view'),
    path('brands/', views.CarBrandListView.as_view(), name='car_brand_list_view'),

    path('model/<int:pk>', views.CarModelDetailView.as_view(), name='car_model_detail_view'),
    path('models/', views.CarModelListView.as_view(), name='car_model_list_view'),

    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order_detail_view'),
    path('orders/', views.OrderListView.as_view(), name='order_list_view'),
    path('orders/<str:sorted>', views.OrderListView.as_view(), name='order_list_view_sorted'),
    path('order/<str:brand>', views.OrderFilterListView.as_view(), name='order_filter_list_view'),

    path('count_order_colors/', views.CountOrderColorsListView.as_view(), name='count_order_colors'),
    path('count_order_brands/', views.CountOrderBrandsListView.as_view(), name='count_order_brands'),

]
