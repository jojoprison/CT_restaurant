from django.urls import path

from restaurant.views import *

urlpatterns = [
    path('api/v1/foods/', FoodListViewSet.as_view({'get': 'list'})),
    path('api/v1/foods/<int:pk>/', FoodListViewSet.as_view({'get': 'retrieve'}))
]
