from django.contrib import admin
from django.contrib.auth.models import Group
from restaurant.models import *

admin.site.unregister(Group)
admin.site.register(Food)
admin.site.register(FoodCategory)
