import pytest
import json
from food.serializers import VegetableSerializer, VegetableTypeSerializer


@pytest.mark.django_db
class TestSerializer:
    @pytest.fixture(autouse=True)
    def create_vegetable_type(self):
        veg_type = {"name": "fruit"}
        VegetableTypeSerializer.create(self, data=veg_type)
        yield

    def test_vegetable_serializer(self):
        input_vegetable = json.loads(
            open("food/tests/files/create_and_return_ok.json").read()
        )

        result = VegetableSerializer(data=input_vegetable)

        if result.is_valid(raise_exception=True):
            assert result.data == input_vegetable
