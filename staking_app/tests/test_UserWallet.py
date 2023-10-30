from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from staking_app.models import UserWallet

UserWallet_URL = reverse("staking:user_wallet-list")


class UnauthentikatedWalletApiTest(TestCase):
    """
    Checking that only authenticated user can have access to endpoint
    """
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(UserWallet_URL)
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class UserWalletCreationTest(TestCase):
    """
    Checking ability to create UserWallet instance
    """
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="testpass",
        )
        self.user_wallet = UserWallet.objects.create(user=self.user, balance=1000)

    def test_user_wallet_creation(self):
        self.assertEqual(self.user_wallet.user, self.user)
        self.assertEqual(self.user_wallet.balance, 1000.00000)




