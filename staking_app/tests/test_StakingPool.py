from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from staking_app.models import StakingPool

Staking_Pool_URL = reverse("staking:staking_pool-list")


class UnauthentikatedStakingPoolApiTest(TestCase):
    """
    Checking that only authenticated user can have access to endpoint
    """
    
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(Staking_Pool_URL)
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class StakingPoolTest(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create(email="test1@example.com")
        self.user2 = get_user_model().objects.create(email="test2@example.com")
        self.staking_pool = StakingPool.objects.create(
            name="Pool A",
            description="This is a staking pool for testing purposes."
        )
        self.staking_pool.stak_holders.add(self.user1, self.user2)

    def test_staking_pool_creation(self):
        self.assertEqual(self.staking_pool.name, "Pool A")
        self.assertEqual(self.staking_pool.description, "This is a staking pool for testing purposes.")

    def test_staking_pool_str_method(self):
        expected_string = "Pool A"
        self.assertEqual(str(self.staking_pool), expected_string)

    def test_staking_pool_stak_holders(self):
        self.assertEqual(self.staking_pool.stak_holders.count(), 2)