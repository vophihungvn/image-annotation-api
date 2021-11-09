from django.urls import reverse
from api.models import Label
from .test_base import BaseTestCase


class TestDefaultView(BaseTestCase):
    """
        Testcases for API views
    """

    def test_can_call_default_route_success(self):
        res = self.client.get(reverse("default"))
        self.assertEquals(res.status_code, 200)


class TestLabelRoute(BaseTestCase):
    """
        Testcases for API routes
    """

    def setUp(self) -> None:
        Label.objects.create(
            name="Car",
            category="Vehicle"
        )
        return super().setUp()

    def test_get_list_label(self):
        res = self.client.get(reverse("label"), format="json")
        self.assertEquals(res.status_code, 200)
        self.assertEquals(len(res.data['data']), 1)

    def test_create_label(self):
        self.client.post(reverse("label"), {
            "name": "Bike",
            "category": "Vehicle"
        },  format="json")

        res = self.client.get(reverse("label"), format="json")
        self.assertEquals(len(res.data['data']), 2)

    def test_modify_label(self):
        res = self.client.put(
            reverse("label-item",  kwargs={'id': 1}),
            {"name": "Motorbike"},
            format="json"
        )
        res = self.client.get(
            reverse("label-item", kwargs={'id': 1}), format="json")
        self.assertEquals(res.data['data']['name'], 'Motorbike')

    def test_delete_label(self):
        res = self.client.delete(
            reverse("label-item",  kwargs={'id': 1})
        )

        res = self.client.get(reverse("label"), format="json")
        self.assertEquals(len(res.data['data']), 0)
