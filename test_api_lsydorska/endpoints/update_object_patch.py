from test_api_lsydorska.endpoints.endpoint import Endpoint
import requests
import allure

class UpdateObjectPatch(Endpoint):

    @allure.step('Send patch request')
    def patch_changes_in_object(self, object_id, body):
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body
        )
        self.json = self.response.json()
        return self.response
