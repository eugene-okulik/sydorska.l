from locust import task, HttpUser, SequentialTaskSet
import random


class CreateGetDelete(SequentialTaskSet):
    object_id = None

    @task
    def create_object(self):
        response = self.client.post(
            '/object',
            json={
                "name": "test_for_locus_LS",
                "data": {
                    "color": "white",
                    "size": "medium"
                }
            }
        )
        self.object_id = response.json()['id']

    @task
    def get_newest_created_object(self):
        self.client.get(f'/object/{self.object_id}')

    @task
    def delete_new_object(self):
        self.client.delete(f'/object/{self.object_id}')
        self.interrupt()


class ObjectBasicUser(HttpUser):
    tasks = [CreateGetDelete]
    min_wait = 1000
    max_wait = 3000

    @task(1)
    def get_all_objects(self):
        self.client.get('/object')

    @task(2)
    def get_one_random_existing_objects(self):
        self.client.get(f'/object/{random.choice([3074, 3118, 3159])}')
