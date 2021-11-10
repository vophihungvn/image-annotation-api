from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import response
from django.urls import reverse
from api.models import Label
from api.tests.test_base import BaseTestCase


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
            category="Vehicle",
            created_by=1
        )
        return super().setUp()

    def get_list_labels(self):
        """Internal util func"""
        res = self.client.get(reverse("label"), format="json")
        return res

    def test_get_list_label(self):
        """Test label successfullt retrived"""
        res = self.get_list_labels()
        self.assertEquals(res.status_code, 200)
        self.assertEquals(len(res.data['data']), 1)

    def test_create_label(self):
        """Check if new label can created sucessfully"""
        self.client.post(reverse("label"), {
            "name": "Bike",
            "category": "Vehicle"
        },  format="json")

        res = self.get_list_labels()
        self.assertEquals(len(res.data['data']), 2)

    def test_modify_label(self):
        """Check if label can be modified"""
        res = self.client.put(
            reverse("label-item",  kwargs={'id': 1}),
            {"name": "Motorbike"},
            format="json"
        )
        res = self.client.get(
            reverse("label-item", kwargs={'id': 1}), format="json")
        self.assertEquals(res.data['data']['name'], 'Motorbike')

    def test_delete_label(self):
        """Check if label can be deleted"""
        res = self.client.delete(
            reverse("label-item",  kwargs={'id': 1})
        )

        res = self.get_list_labels()
        self.assertEquals(len(res.data['data']), 0)

    def test_user_can_access_own_result(self):
        """Check if another one can not access resource"""
        res = self.get_list_labels()
        self.assertEquals(len(res.data['data']), 1)

        self.client.force_authenticate(self.user2)
        res = self.get_list_labels()
        self.assertEquals(len(res.data['data']), 0)


class TestImageRoutes(BaseTestCase):
    """
        Test image route
    """

    def setUp(self) -> None:
        Label.objects.create(
            name="Car",
            category="Vehicle",
            created_by=1
        )
        return super().setUp()

    def create_image(self):
        """Util function to create image"""
        file = SimpleUploadedFile(
            "file.png", b"sample_image", content_type="image/png")
        payload = {"image": file}
        response = self.client.post(
            reverse('image'), payload, format="multipart")
        return response

    def create_tag(self):
        """Util function to create tag"""
        response = self.client.post(reverse('image-tag', kwargs={'id': 1}), {
            "label_id": 1,
            "position": {
                "top": 100,
                "left": 100,
                "width": 100,
                "height": 100
            }
        }, format='json')

        return response

    def test_create_image(self):
        """Check if image can be created"""
        response = self.create_image()
        self.assertEqual(response.status_code, 200)

    def test_retrieve_label_by_id(self):
        """Check if created image can be retrieved"""
        self.create_image()

        response = self.client.get(reverse('image-item', kwargs={'id': 1}))
        self.assertEquals(response.data['data']['id'], 1)

    def test_create_image_tag_successfully(self):
        """Check if new tag can be created"""
        self.create_image()

        response = self.create_tag()

        self.assertEqual(response.status_code, 200)
        self.assertEquals(response.data['data']['id'], 1)

    def test_create_tag_with_image_not_exists(self):
        """Check if creating tag should raise error if image not exists"""
        response = self.create_tag()

        self.assertEqual(response.status_code, 404)
