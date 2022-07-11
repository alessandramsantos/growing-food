import pytest
import json
from food.serializers import VegetableSerializer, VegetableTypeSerializer
from food.models import Vegetable, VegetableType


@pytest.mark.django_db
class TestSerializer:
    @pytest.fixture
    def create_vegetable_type(self):
        veg_type = {"id": 1, "name": "fruit"}
        VegetableType.objects.create(**veg_type)

    def test_vegetable_type_serializer(self):
        input_vegetable_type = {"name": "fruit"}
        serializer = VegetableTypeSerializer(data=input_vegetable_type)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            del data["id"]
            assert data == input_vegetable_type
            assert VegetableType.objects.count() == 1

    def test_vegetable_serializer(self, create_vegetable_type):
        input_vegetable = json.loads(
            open("food/tests/files/create_and_return_ok.json").read()
        )

        serializer = VegetableSerializer(data=input_vegetable)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = serializer.data
            del data["id"]
            del data["created"]
            assert data == input_vegetable
            assert Vegetable.objects.count() == 1