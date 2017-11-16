from rest_framework import status
from rest_framework.test import APITestCase

from account.models import User


class AccountTests(APITestCase):
    """Test user's endpoints."""
    def test_create_account(self):
        """It should create correctly an User."""
        url = '/users/'
        data = {
            "is_superuser": False,
            "username": "test",
            "first_name": "Testing",
            "last_name": "Testings",
            "email": "test@test.com",
            "is_staff": False,
            "is_active": True,
            "user_type": "S",
            "social_number": "11111111111",
            "address": "test",
            "payment_status": "NPR",
            "phone_number": "5561999999999",
            "gender": "M",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

