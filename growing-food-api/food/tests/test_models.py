import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestModels:
    client = APIClient()

    def test_vegetables(self):
        pass

    def test_post_vegetable(self):
        new_vegetable = {
            "name": "Cucumber",
            "description": "Cucumber",
            "compost": "Dirt",
            "harvest": "2 months",
            "watering": 2,
            "veg_type": 2,
        }

        response = self.client.post("/vegetable-create", new_vegetable)
        assert response.status_code == 201
        assert response.json()["name"] == new_vegetable["name"]

    def test_get_vegetables(self):
      response = self.client.get("/vegetables/")
      assert response.status_code == 200

    def test_get_vegetable(self):
      pass