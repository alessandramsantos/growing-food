import pytest
import json
from food.serializers import VegetableSerializer


@pytest.mark.django_db
class TestSerializer:
    def test_vegetable_serializer(self):
        
        input_vegetable = {
            "name": "potato",
            "description": "",
            "compost": "Dirt",
            "harvest": "3 months",
            "watering": 1,
            "veg_type": 1,
        }
        result = VegetableSerializer(data=input_vegetable)

        if result.is_valid(raise_exception=True):
            return "ok"

        # Error: rest_framework.exceptions.ValidationError: {'veg_type': [ErrorDetail(string='Invalid pk "1" - object does not exist.', code='does_not_exist')]}

# Steps:
#  input_vegetable = JSON(ETC)
# result = serializer.create(input_vegetable)
# CONVERT result TO JSON HERE
# assert CONVERED is equal to INPUT