
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class BaseTestCase(APITestCase):

    def setUp(self) -> None:
        username = 'fake-user'
        password = 'F@k3P@ssw0rd'
        self.user = User.objects.create_user(username, password)
        self.user2 = User.objects.create_user('user-2', password)
        self.client.force_authenticate(self.user)
        return super().setUp()
