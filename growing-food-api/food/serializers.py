from rest_framework import serializers
from food.models import VegetableType, Vegetable

class VegetableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta receives two parameters: model and fields.
        We can specify the fields like ['id', 'name', 'created'] or have them all"""
        model = VegetableType
        fields = '__all__'
    
    def create(self, data):
        return VegetableType.objects.create(**data)


class VegetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegetable
        fields = '__all__'

    def create(self, data):
        return Vegetable.objects.create(**data)
