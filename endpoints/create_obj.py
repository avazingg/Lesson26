import requests
import jsonschema
from endpoints.base_endpoint import Endpoint
from payload.payload import valid_create_payload


class CreateObj(Endpoint):
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "data": {
                "type": "object",
                "properties": {
                    "year": {"type": "integer"},
                    "price": {"type": "number"},
                    "CPU model": {"type": "string"},
                    "Hard disk size": {"type": "string"}
                },
                "required": ["year", "price", "CPU model", "Hard disk size"]
            }
        },
        "required": ["id", "name", "data"]
    }

    def new_obj(self, payload):
        self.response = requests.post(f'{self.url}/objects',
                                      json=payload)
        self.response_json = self.response.json()


    def get_name(self):
        return self.get_data()['name']

    def get_year(self):
        return self.get_data()['data']['year']

    def get_price(self):
        return self.get_data()['data']['price']

    def get_cpu_model(self):
        return self.get_data()['data']['CPU model']

    def get_hard_disk_size(self):
        return self.get_data()['data']['Hard disk size']

    def get_all_fields(self):
        return self.get_data()["data"]

    def check_all_fields(self, expected_data):
        assert self.get_data()["data"] == expected_data["data"], "wrong data in it"
