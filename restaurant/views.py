from rest_framework import viewsets

from restaurant.serializers import *


class FoodListViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        if self.action == 'retrieve':
            return FoodCategory.objects.filter(pk=self.kwargs.get('pk'))
        else:
            category_ids = Food.objects.filter(is_publish=True).values_list('category_id', flat=True)
            return FoodCategory.objects.filter(id__in=category_ids)
