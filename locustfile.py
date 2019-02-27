# this is the path almost everyone will take:
# https://happybabycarriers.com/
# https://happybabycarriers.com/shop/
# https://happybabycarriers.com/shop/happy-baby-carrier/ (pick a color)
# https://happybabycarriers.com/cart/
# https://happybabycarriers.com/checkout/


from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):


    @task(1)
    def index(self):
        self.client.get("/")

    @task(2)
    def shop(self):
        self.client.get("/shop/")

    @task(3)
    def product(self):
        self.client.get("/shop/happy-baby-carrier/")

    @task(4)
    def product(self):
        self.client.get("/cart/")

    @task(5)
    def product(self):
        self.client.get("/checkout/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 15000
    max_wait = 30000
