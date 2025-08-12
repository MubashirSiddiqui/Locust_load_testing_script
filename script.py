from locust import HttpUser, task, between
# Single URL load Attempt

class QuickLoadTest(HttpUser):
    wait_time = between(0, 0)  # no wait between tasks

    @task
    def hit_endpoint(self):
        self.client.get("/")  # root path of your domain

# To run:
# locust -f locustfile.py --host=http://azaadi-preprod.golootlo.pk
