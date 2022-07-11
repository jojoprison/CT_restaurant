from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed

from restaurant.serializers import *


class FoodListViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return FoodCategory.objects.all()
        elif self.action == 'retrieve':
            return FoodCategory.objects.filter(pk=self.kwargs.get('pk'))
        else:
            raise MethodNotAllowed

    def get_serializer_class(self):
        if self.action == 'list':
            return FoodListSerializer
        if self.action == 'retrieve':
            return FoodListSerializer
