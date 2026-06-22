from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class RegistrationTests(APITestCase):

    def setUp(self):
        self.url = "/api/registration/"

    def test_registration_success(self):
        payload = {
            "username": "newuser",
            "email": "new@test.de",
            "password": "test123456",
            "repeated_password": "test123456",
            "type": "customer"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)

    def test_password_mismatch(self):
        payload = {
            "username": "newuser",
            "email": "new@test.de",
            "password": "test123456",
            "repeated_password": "wrong",
            "type": "customer"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_email(self):
        User.objects.create_user(
            username="existing",
            email="dup@test.de",
            password="test123456",
            type="customer"
        )

        payload = {
            "username": "newuser",
            "email": "dup@test.de",
            "password": "test123456",
            "repeated_password": "test123456",
            "type": "customer"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_missing_fields(self):
        payload = {
            "username": "",
            "email": "",
            "password": "",
            "repeated_password": "",
            "type": "customer"
        }

        response = self.client.post(self.url, payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)