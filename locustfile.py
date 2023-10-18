from locust import HttpUser, task


class Resume(HttpUser):
    @task
    def homepage(self):
        self.client.get("")


class Blog(HttpUser):
    @task
    def posts_list(self):
        self.client.get("/blog")

    @task
    def tags_list(self):
        self.client.get("/blog/tags")


class Scan(HttpUser):
    @task
    def main_page(self):
        self.client.get("/scan")
