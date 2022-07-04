import pytest
import requests
from httmock import HTTMock
from food.tests import api_mocks
# from food.models import Vegetable


@pytest.mark.django_db
class TestViews:

    BASE_URL = "http://localhost:8000"

    @pytest.fixture(autouse=True)
    def vegetable_mock_http_request(self):
        with HTTMock(
            api_mocks.vegetable_create_and_return_ok,
            api_mocks.vegetable_get_and_return_ok,
            api_mocks.vegetable_get_details_and_return_ok,
            api_mocks.vegetable_delete_and_return_ok,
            api_mocks.vegetable_update_and_return_ok,
        ):
            yield

    def test_get_vegetables(self):
        response = requests.get(f"{self.BASE_URL}/vegetables/")
        assert response.status_code == 200
        assert len(response.json()) == 2

    def test_post_vegetable(self):
        new_vegetable = {
            "name": "Cucumber",
            "description": "Cucumber",
            "compost": "Dirt",
            "harvest": "2 months",
            "watering": 2,
            "veg_type": 2,
        }
        response = requests.post(f"{self.BASE_URL}/vegetable-create", new_vegetable)

        assert response.status_code == 201
        assert response.json()["name"] == new_vegetable["name"]

    def test_get_vegetable(self):
        response = requests.get(f"{self.BASE_URL}/vegetable/2")

        assert response.status_code == 200
        assert response.json()["id"] == 2

    def test_update_vegetable(self):
        updated_name = {"name": "Carrot"}
        response = requests.put(f"{self.BASE_URL}/vegetable/2", updated_name)

        assert response.status_code == 200
        assert response.json()["name"] == updated_name["name"]

    def test_delete_vegetable(self):
        response = requests.delete(f"{self.BASE_URL}/vegetable/2")

        assert response.status_code == 204
        assert response.json() == {}
        # assert Vegetable.objects.filter(id=2).count() == 0