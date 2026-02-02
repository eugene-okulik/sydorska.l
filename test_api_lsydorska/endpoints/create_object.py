import requests
import allure
from test_api_lsydorska.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):

    def __init__(self):
        self.object_id = None

    @allure.step('Create new object')
    def new_object_id(self, body):
        self.response = requests.post(self.url, json=body)
        self.json = self.response.json()
        self.object_id = self.json['id']
        return self.response
