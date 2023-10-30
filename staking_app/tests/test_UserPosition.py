from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status, serializers

from rest_framework.test import APIClient

from staking_app.models import UserPosition, UserWallet
from user.models import User

UserPosition_URL = reverse("staking:user_position-list")


class UnauthentikatedUserPositionApiTest(TestCase):
    """
    Checking that only authenticated user can have access to endpoint
    """
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(UserPosition_URL)
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class UserPositionCreationTest(TestCase):
    """
    Checking ability to create UserWallet instance
    """
    def setUp(self):
        self.user = User.objects.create(email="test@example.com")
        self.user_wallet = UserWallet.objects.create(user=self.user, balance=5000.00000)
        self.user_position = UserPosition.objects.create(
            user=self.user, amount=2000.00000, cryptocurrency="bitcoin"
        )

    def test_user_position_creation(self):
        self.assertEqual(self.user_position.user, self.user)
        self.assertEqual(self.user_position.amount, 2000.00000)
        self.assertEqual(self.user_position.cryptocurrency, "bitcoin")






