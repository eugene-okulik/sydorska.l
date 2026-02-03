import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object_put import UpdateObjectPut
from endpoints.update_object_patch import UpdateObjectPatch
from test_api_lsydorska.endpoints.delete import DeleteObject
from test_api_lsydorska.endpoints.get_object import GetObject


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


@pytest.fixture()
def create_new_object():
    return CreateObject()


@pytest.fixture()
def update_object_put():
    return UpdateObjectPut()


@pytest.fixture()
def update_object_patch():
    return UpdateObjectPatch()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def create_object_id(create_new_object, delete_object_endpoint):
    body = {"name": "new post by LS", "data": {"color": "multy", "size": "small"}}
    response = create_new_object.new_object_id(body)
    object_id = response.json()["id"]
    print(f'Create id {object_id}')
    yield object_id
    print(f'Delete id {object_id}')
    delete_object_endpoint.delete_object(object_id)


@pytest.fixture()
def get_object_endpoint():
    return GetObject()
