from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APIClient

from staking_app.models import StakingPool, PoolConditions

PoolConditions_URL = reverse("staking:pool_conditions-list")


class UnauthentikatedPoolConditionApiTest(TestCase):
    """
    Checking that only authenticated user can have access to endpoint
    """

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(PoolConditions_URL)
        self.assertEquals(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PoolConditionsCreationTest(TestCase):
    """
    Checking ability to create PoolCondition instance
    """

    def setUp(self):
        self.pool = StakingPool.objects.create(
            name="Test Pool", description="Test Description"
        )
        self.pool_condition = PoolConditions.objects.create(
            pool=self.pool, minimum_stake=1000.00000, annual_percentage_yield=5.0
        )

    def test_pool_conditions_creation(self):
        self.assertEqual(self.pool_condition.pool, self.pool)
        self.assertEqual(self.pool_condition.minimum_stake, 1000.00000)
        self.assertEqual(self.pool_condition.annual_percentage_yield, 5.0)
