import pytest
import allure


@allure.description('Test POST method for one object (create new object)')
@pytest.mark.parametrize('name', ['new post 1', 'new post 2', 'new post 3'])
def test_create_new_object(create_new_object, test_session, each_test, name):
    body = {"name": name, "data": {"color": "white", "size": "medium"}}
    response = create_new_object.new_object_id(body)
    response_json = response.json()
    create_new_object.check_status_code_is_correct()
    create_new_object.check_name_is_correct(body['name'])
    create_new_object.check_color_is_correct(response_json)
    create_new_object.check_size_is_correct(response_json)


@allure.description('Test GET method for one object')
def test_one_object(create_object_id, each_test, get_object_endpoint):
    response = get_object_endpoint.get_object(create_object_id)
    get_object_endpoint.check_id_is_correct(response)


@allure.description('Test PUT method for one object')
def test_upd_put_object(update_object_put, create_object_id, each_test):
    body = {
        "name": "new object by LS upd by put",
        "data": {
            "color": "multy upd",
            "size": "small upd"
        }
    }
    response = update_object_put.put_changes_in_object(create_object_id, body)
    update_object_put.check_status_code_is_correct()
    update_object_put.check_name_is_correct(body['name'])
    update_object_put.check_color_is_correct(response.json())
    update_object_put.check_size_is_correct(response.json())


@allure.description('Test PATCH method for one object')
def test_upd_patch_object(update_object_patch, create_object_id, each_test):
    body = {
        "name": "new object by LS upd by patch",
        "data": {
            "size": "small patch"
        }
    }
    response = update_object_patch.patch_changes_in_object(create_object_id, body)
    update_object_patch.check_status_code_is_correct()
    update_object_patch.check_name_is_correct(body['name'])
    update_object_patch.check_size_is_correct(response.json())


@allure.description('Test DELETE method for one object')
def test_create_delete_object(delete_object_endpoint, create_object_id, each_test):
    response = delete_object_endpoint.delete_object(create_object_id)
    delete_object_endpoint.check_status_code_is_correct()
    delete_object_endpoint.check_message_after_delete_the_object(response, create_object_id)
