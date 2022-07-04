from httmock import urlmatch
from rest_framework import status


@urlmatch(path="/vegetable-create", method="POST")
def vegetable_create_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_201_CREATED,
        "content": open("food/tests/files/create_and_return_ok.json").read(),
    }

@urlmatch(path="/vegetables", method="GET")
def vegetable_get_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": open(
            "food/tests/files/get_and_return_ok.json"
        ).read(),
    }

@urlmatch(path="/vegetable/2", method="GET")
def vegetable_get_details_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": open("food/tests/files/get_details_and_return_ok.json").read(),
    }

@urlmatch(path="/vegetable/2", method="PUT")
def vegetable_update_and_return_ok(url, request):
    return {"status_code": status.HTTP_200_OK, "content": open("food/tests/files/update_and_return_ok.json").read(),}
    


@urlmatch(path="/vegetable/2", method="DELETE")
def vegetable_delete_and_return_ok(url, request):
    return {"status_code": status.HTTP_204_NO_CONTENT, "content": {}}


