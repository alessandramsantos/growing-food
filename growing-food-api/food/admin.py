from django.contrib import admin
from food.models import Vegetable, VegetableType

class Vegetables(admin.ModelAdmin):
    list_display = ('id', 'name', 'veg_type')
    list_display_links = ('id', 'name', 'veg_type')
    search_fields = ('name',)



class VegetablesType(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Vegetable, Vegetables)
admin.site.register(VegetableType, VegetablesType)