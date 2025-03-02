from conftest import valid_created_obj, create_obj
from endpoints.create_obj import CreateObj
from endpoints.delete_obj import DeleteObj
from endpoints.update_obj import UpdateObj
from payload.payload import valid_create_payload, updated_payload
from endpoints import delete_obj

def test_delete_obj():
    #create obj
    obj = CreateObj()
    obj.new_obj(payload=valid_create_payload)
    obj.check_response_is_200()
    obj.validate(obj.get_data())
    obj.check_all_fields(valid_create_payload)

    #read obj
    get_data = obj.get_data()
    print(get_data)

    #update obj
    update_obj = UpdateObj()
    update_obj.update_obj(get_data["id"], updated_payload)
    update_obj.check_all_fields(updated_payload)

    #delete obj
    delete_obj = DeleteObj()
    delete_obj.delete_obj(obj.get_data()['id'])
    delete_obj.check_response_is_200()
    delete_obj.validate(delete_obj.get_data())

    assert 'deleted' in delete_obj.get_delete_message(), "wrong message"

