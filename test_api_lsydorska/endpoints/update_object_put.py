from test_api_lsydorska.endpoints.endpoint import Endpoint
import requests
import allure


class UpdateObjectPut(Endpoint):

    @allure.step('Send put request')
    def put_changes_in_object(self, object_id, body):
        self.response = requests.put(
            f'{self.url}/{object_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response
