from rest_framework import serializers

from restaurant.models import *


class FoodFilteredListSerializer(serializers.ListSerializer):
    def to_representation(self, instance):
        instance = instance.filter(is_publish=True)
        return super(FoodFilteredListSerializer, self).to_representation(instance)


class FoodSerializer(serializers.ModelSerializer):
    additional = serializers.SlugRelatedField(many=True, read_only=True, slug_field='internal_code')

    class Meta:
        list_serializer_class = FoodFilteredListSerializer
        model = Food
        fields = ('internal_code', 'code', 'name_ru', 'description_ru', 'description_en',
                  'description_ch', 'is_vegan', 'is_special', 'cost', 'additional')

class FoodListSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(source='food', many=True, read_only=True)

    class Meta:
        model = FoodCategory
        fields = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id', 'foods')
