import pytest
import requests


@pytest.fixture(scope='session')
def test_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def each_test():
    print('before test')
    yield
    print('after test')


@pytest.mark.parametrize('name', ['new post 1', 'new post 2', 'new post 3'])
def test_create_new_post(test_session, each_test, name):
    body = {
        "name": name,
        "data": {
            "color": "white",
            "size": "medium"
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body
    )
    assert response.status_code == 200, 'Status code is incorect'
    assert response.json()['name'] == name, 'Name is incorrect'
    assert response.json()['data']['color'] == "white", "Color is incorect"
    assert response.json()['data']['size'] == "medium", "Size is incorect"


@pytest.fixture()
def new_post_id():
    body = {
        "name": "new post by LS",
        "data": {
            "color": "multy",
            "size": "small"
        }
    }
    response = requests.post(
        "http://objapi.course.qa-practice.com/object",
        json=body
    )
    post_id = response.json()['id']
    yield post_id
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')


# @pytest.fixture()
# def clear(new_post_id):
#     requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')


def test_one_post(new_post_id, each_test):
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    assert response.json()['id'] == new_post_id


@pytest.mark.critical
def test_upd_put_post(new_post_id, each_test):
    body = {
        "name": "new post by LS upd by put",
        "data": {
            "color": "multy upd",
            "size": "small upd"
        }
    }
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorect'
    assert response.json()['name'] == 'new post by LS upd by put', 'Title does not agreed'
    assert response.json()['data']['color'] == 'multy upd', 'Color does not agreed'
    assert response.json()['data']['size'] == 'small upd', 'Size does not agreed'


@pytest.mark.medium
def test_upd_patch_post(new_post_id, each_test):
    body = {
        "name": "new post by LS upd by patch",
        "data": {
            "size": "small patch"
        }
    }
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{new_post_id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorect'
    assert response.json()['name'] == 'new post by LS upd by patch', 'Name does not agreed'
    assert response.json()['data']['size'] == 'small patch', 'Size does not agreed'


def test_create_delete_post(new_post_id, each_test):
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{new_post_id}')
    assert response.status_code == 200, 'Status code is incorect'
    assert response.text == (f'Object with id {new_post_id} successfully deleted'), 'Text message is incorect'
