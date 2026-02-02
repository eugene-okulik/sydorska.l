from test_api_lsydorska.endpoints.endpoint import Endpoint
import requests
import allure


class DeleteObject(Endpoint):

    @allure.step('Delete an object')
    def delete_object(self, object_id):
        self.response = requests.delete(
            f'{self.url}/{object_id}')
        return self.response

    @allure.step('Validate that correct text message returned after object deleted')
    def check_message_after_delete_the_object(self, response, object_id):
        assert response.text == (
            f'Object with id {object_id} successfully deleted'), 'Text message is incorrect'
