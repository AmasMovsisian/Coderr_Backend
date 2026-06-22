from rest_framework import status
from offers.models import Offer
from tests.base import BaseAPITestCase


class OfferTests(BaseAPITestCase):

    def setUp(self):
        self.business, self.token = self.create_business()

        self.url = "/api/offers/"

        self.payload = {
            "title": "Logo Design",
            "description": "Professional Logo",
            "details": [
                {
                    "title": "Basic",
                    "revisions": 1,
                    "delivery_time_in_days": 3,
                    "price": 50,
                    "features": ["Logo"],
                    "offer_type": "basic"
                },
                {
                    "title": "Standard",
                    "revisions": 2,
                    "delivery_time_in_days": 5,
                    "price": 100,
                    "features": ["Logo", "Business Card"],
                    "offer_type": "standard"
                },
                {
                    "title": "Premium",
                    "revisions": 3,
                    "delivery_time_in_days": 7,
                    "price": 200,
                    "features": ["Logo", "Business Card", "Letterhead"],
                    "offer_type": "premium"
                }
            ]
        }

    def test_create_offer_success(self):
        self.authenticate(self.token)

        response = self.client.post(self.url, self.payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Offer.objects.count(), 1)

    def test_customer_cannot_create_offer(self):
        customer, token = self.create_customer()
        self.authenticate(token)

        response = self.client.post(self.url, self.payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_create_offer(self):
        response = self.client.post(self.url, self.payload, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_offer_list(self):
        self.authenticate(self.token)

        self.client.post(self.url, self.payload, format="json")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_retrieve(self):
        self.authenticate(self.token)

        create = self.client.post(self.url, self.payload, format="json")
        offer_id = create.data["id"]

        response = self.client.get(f"{self.url}{offer_id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_offer_delete(self):
        self.authenticate(self.token)

        create = self.client.post(self.url, self.payload, format="json")
        offer_id = create.data["id"]

        response = self.client.delete(f"{self.url}{offer_id}/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_offer_not_found(self):
        self.authenticate(self.token)

        response = self.client.get(f"{self.url}99999/")

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_invalid_offer_payload(self):
        self.authenticate(self.token)

        response = self.client.post(
            self.url, {"title": "", "details": []}, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
