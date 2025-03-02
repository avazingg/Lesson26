import requests
from endpoints.base_endpoint import Endpoint

class UpdateObj(Endpoint):
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

    def update_obj(self, obj_id, payload):
        self.response = requests.put(f"{self.url}/objects/{obj_id}", json = payload)
        self.response_json = self.response.json()
