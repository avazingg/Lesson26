from conftest import valid_created_obj
from endpoints.create_obj import CreateObj
from endpoints.delete_obj import DeleteObj
from endpoints.update_obj import UpdateObj
from payload.payload import updated_payload


def test_update_obj(valid_created_obj):
    obj_id = valid_created_obj
    update_obj = UpdateObj()
    update_obj.update_obj(obj_id= obj_id,payload= updated_payload)
    print(update_obj.get_data())
