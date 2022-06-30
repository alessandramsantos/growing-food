from httmock import urlmatch

@urlmatch(path="/vegetable-create", method="POST")
def vegetable_create_and_return_ok(request):
    return {"status_code": 201, "content": {
            "name": "Cucumber",
            "description": "Cucumber",
            "compost": "Dirt",
            "harvest": "2 months",
            "watering": 2,
            "veg_type": 2,
        }}


@urlmatch(path="/vegetable/2", method="DELETE")
def vegetable_delete_and_return_ok(request):
    return {"status_code": 200, "content": {"delete"}}

@urlmatch(path="/vegetable/2", method="PUT")
def vegetable_update_and_return_ok(request):
    return {"status_code": 200, "content": {"put"}}


@urlmatch(path="/vegetables", method="GET")
def vegetable_get_and_return_ok(request):
    return {"status_code": 200, "content": {[
    {
        "id": 2,
        "name": "Allium",
        "description": "",
        "compost": "Dirt",
        "harvest": "3 months",
        "watering": 1,
        "created": "2022-06-08T00:28:32.880314Z",
        "veg_type": 2
    },
    {
        "id": 17,
        "name": "carrot",
        "description": "",
        "compost": "Dirt",
        "harvest": "3 months",
        "watering": 1,
        "created": "2022-06-30T18:12:46.104877Z",
        "veg_type": 2
    }
]}}


@urlmatch(path="/vegetable/2", method="GET")
def vegetable_get_detail_and_return_ok(request):
    return {"status_code": 200, "content": {
        "id": 2,
        "name": "Allium",
        "description": "",
        "compost": "Dirt",
        "harvest": "3 months",
        "watering": 1,
        "created": "2022-06-08T00:28:32.880314Z",
        "veg_type": 2
    }}