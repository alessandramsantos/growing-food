from httmock import urlmatch
from rest_framework import status


@urlmatch(path="/vegetable", method="POST")
def vegetable_create_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_201_CREATED,
        "content": open("food/tests/files/create_and_return_ok.json").read(),
    }


@urlmatch(path="/vegetables", method="GET")
def vegetable_get_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": open("food/tests/files/get_and_return_ok.json").read(),
    }


@urlmatch(path="/vegetable/2", method="GET")
def vegetable_get_details_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": open("food/tests/files/get_details_and_return_ok.json").read(),
    }


@urlmatch(path="/vegetable/2", method="PUT")
def vegetable_update_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": open("food/tests/files/update_and_return_ok.json").read(),
    }


@urlmatch(path="/vegetable/2", method="DELETE")
def vegetable_delete_and_return_ok(url, request):
    return {"status_code": status.HTTP_204_NO_CONTENT, "content": {}}


@urlmatch(path="/vegetable-type", method="POST")
def vegetable_type_create_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_201_CREATED,
        "content": {"name": "Allium"},
    }


@urlmatch(path="/vegetable-types", method="GET")
def vegetable_types_get_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": {"name": "Allium"},
    }


@urlmatch(path="/vegetable-type/1", method="GET")
def vegetable_type_get_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": {
            "id": 1,
            "name": "Allium",
        },
    }


@urlmatch(path="/vegetable-type/1", method="PUT")
def vegetable_type_update_and_return_ok(url, request):
    return {
        "status_code": status.HTTP_200_OK,
        "content": {"name": "Leafy Green"},
    }


@urlmatch(path="/vegetable-type/1", method="DELETE")
def vegetable_type_delete_and_return_ok(url, request):
    return {"status_code": status.HTTP_204_NO_CONTENT, "content": {}}
