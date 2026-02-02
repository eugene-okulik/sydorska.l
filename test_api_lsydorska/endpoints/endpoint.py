import allure


class Endpoint:
    url = 'http://objapi.course.qa-practice.com/object'
    response = None
    json = None

    @allure.step('Validate 200 status code')
    def check_status_code_is_correct(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Validate the name is agreed')
    def check_name_is_correct(self, name):
        assert self.json['name'] == name, 'Name is incorrect'

    @allure.step('Validate color fom data')
    def check_color_is_correct(self, response):
        assert response['data']['color'] == response['data']['color'], "Color is incorrect"

    @allure.step('Validate size fom data')
    def check_size_is_correct(self, response):
        assert response['data']['size'] == response['data']['size'], "Size is incorrect"

    @allure.step(f'Validate that correct id has been returned')
    def check_id_is_correct(self, response):
        with allure.step(f'Validate that id is {response.json()['id']}'):
            assert self.response.json()['id'] == response.json()['id']
