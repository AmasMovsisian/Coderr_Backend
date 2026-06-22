from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from profiles.models import Profile

User = get_user_model()


class BaseAPITestCase(APITestCase):

    def create_customer(self):
        user = User.objects.create_user(
            username="customer",
            email="customer@test.de",
            password="test123456",
            type="customer"
        )

        Profile.objects.create(user=user)
        token = Token.objects.create(user=user)

        return user, token

    def create_business(self):
        user = User.objects.create_user(
            username="business",
            email="business@test.de",
            password="test123456",
            type="business"
        )

        Profile.objects.create(user=user)
        token = Token.objects.create(user=user)

        return user, token

    def authenticate(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def unauthenticate(self):
        self.client.credentials()
