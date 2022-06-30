import pytest
from rest_framework.test import APIClient
from httmock import HTTMock
from food.tests import api_mocks

@pytest.mark.django_db
class TestViews:
    client = APIClient()

    def test_get_vegetables(self):
        pass
      # response = self.client.get("/vegetables/")
      # assert response.status_code == 200
      #get all vegetables

    @pytest.fixture()
    def vegetable_create_mock_http_request(self):
      with HTTMock(
        api_mocks.vegetable_delete_and_return_ok
        ): 
            yield
    
    def test_post_vegetable(self, vegetable_create_mock_http_request):
        new_vegetable = {
            "name": "Cucumber",
            "description": "Cucumber",
            "compost": "Dirt",
            "harvest": "2 months",
            "watering": 2,
            "veg_type": 2,
        }
        response = vegetable_create_mock_http_request()
        # TypeError: 'NoneType' object is not callable


        assert response.status_code == 201
        assert response.json()["name"] == new_vegetable["name"]

    def test_get_vegetable(self):
      pass
    #get vegetable detail


    def test_update_vegetable(self):
      pass
    #update existing vegetable

    def test_delete_vegetable(self):
      pass
    #detele existing vegetable