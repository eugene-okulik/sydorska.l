import requests


def create_new_post():
    body = {
        "name": "new post by LS",
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
    assert response.json()['name'] == "new post by LS", 'Name is incorrect'
    assert response.json()['data']['color'] == "white", "Color is incorect"
    assert response.json()['data']['size'] == "medium", "Size is incorect"


create_new_post()


def new_post():
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
    return response.json()['id']


new_post()


def one_post():
    post_id = new_post()
    response = requests.get(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.json()['id'] == post_id


one_post()


def clear(post_id):
    requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')


def upd_put_post():
    post_id = new_post()
    body = {
        "name": "new post by LS upd by put",
        "data": {
            "color": "multy upd",
            "size": "small upd"
        }
    }
    response = requests.put(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorect'
    assert response.json()['name'] == 'new post by LS upd by put', 'Title does not agreed'
    assert response.json()['data']['color'] == 'multy upd', 'Color does not agreed'
    assert response.json()['data']['size'] == 'small upd', 'Size does not agreed'
    clear(post_id)


upd_put_post()


def upd_patch_post():
    post_id = new_post()
    body = {
        "name": "new post by LS upd by patch",
        "data": {
            "size": "small patch"
        }
    }
    response = requests.patch(
        f'http://objapi.course.qa-practice.com/object/{post_id}',
        json=body
    )
    assert response.status_code == 200, 'Status code is incorect'
    assert response.json()['name'] == 'new post by LS upd by patch', 'Name does not agreed'
    assert response.json()['data']['size'] == 'small patch', 'Size does not agreed'
    clear(post_id)


upd_patch_post()


def delete_post():
    post_id = new_post()
    response = requests.delete(f'http://objapi.course.qa-practice.com/object/{post_id}')
    assert response.status_code == 200, 'Status code is incorect'
    assert response.text == (f'Object with id {post_id} successfully deleted'), 'Text message is incorect'


delete_post()
