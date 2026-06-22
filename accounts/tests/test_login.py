from rest_framework import status
from tests.base import BaseAPITestCase


class LoginTests(BaseAPITestCase):

    def setUp(self):
        self.user, self.token = self.create_customer()
        self.url = "/api/login/"

    def test_login_success(self):
        payload = {
            "username": "customer",
            "password": "test123456"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)

    def test_invalid_password(self):
        payload = {
            "username": "customer",
            "password": "wrong"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_credentials(self):
        payload = {}

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_username(self):
        payload = {
            "username": "doesnotexist",
            "password": "test123456"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
