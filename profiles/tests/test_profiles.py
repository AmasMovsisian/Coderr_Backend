from rest_framework import status
from tests.base import BaseAPITestCase


class ProfileTests(BaseAPITestCase):

    def setUp(self):
        self.user, self.token = self.create_customer()
        self.url = f"/api/profile/{self.user.id}/"

    def test_get_profile_authenticated(self):
        self.authenticate(self.token)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_unauthenticated(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_patch_own_profile(self):
        self.authenticate(self.token)

        response = self.client.patch(
            self.url, {"location": "Berlin"}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_foreign_profile_forbidden(self):
        second_user, _ = self.create_business()

        self.authenticate(self.token)

        response = self.client.patch(
            f"/api/profile/{second_user.id}/",
            {"location": "Berlin"},
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_not_found(self):
        self.authenticate(self.token)

        response = self.client.get("/api/profile/99999/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_business_profiles_list(self):
        self.create_business()
        self.authenticate(self.token)

        response = self.client.get("/api/profiles/business/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_profiles_list(self):
        self.authenticate(self.token)

        response = self.client.get("/api/profiles/customer/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
