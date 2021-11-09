
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class BaseTestCase(APITestCase):

    def setUp(self) -> None:
        username = 'fake-user'
        password = 'F@k3P@ssw0rd'
        user = User.objects.create_user(username, password)
        self.client.force_authenticate(user)
        return super().setUp()
