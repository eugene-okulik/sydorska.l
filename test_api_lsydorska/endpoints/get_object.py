import requests
from test_api_lsydorska.endpoints.endpoint import Endpoint


class GetObject(Endpoint):
    def get_object(self, object_id):
        self.response = requests.get(
            f'{self.url}/{object_id}'
        )
        self.json = self.response.json()
        return self.response
