import pytest

from endpoints.create_obj import CreateObj
from payload import payload
from payload.payload import valid_create_payload


@pytest.fixture
def create_obj():
    return CreateObj()

@pytest.fixture
def valid_created_obj():
    obj = CreateObj()
    obj.new_obj(payload=valid_create_payload)
    obj_id = obj.get_data()["id"]
    yield obj_id
    obj.check_response_is_200()
    obj.validate(obj.get_data())

