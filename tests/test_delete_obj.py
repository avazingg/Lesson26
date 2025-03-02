from conftest import valid_created_obj
from endpoints.create_obj import CreateObj
from endpoints.delete_obj import DeleteObj
from payload.payload import valid_create_payload
from endpoints import delete_obj

def test_delete_obj(valid_created_obj):
    obj_id = valid_created_obj
    delete_obj = DeleteObj()
    delete_obj.delete_obj(obj_id)
    delete_obj.check_response_is_200()
    delete_obj.validate(delete_obj.get_data())

    assert 'deleted' in delete_obj.get_delete_message(), "wrong message"