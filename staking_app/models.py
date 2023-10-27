from django.conf import settings
from django.db import models


class UserWallet(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=20, decimal_places=5)

    def __str__(self):
        return f"{self.user.full_name} wallet({self.balance})"


class UserPosition(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cryptocurrency = models.CharField(max_length=50)  # The specific cryptocurrency name
    amount = models.DecimalField(
        max_digits=20, decimal_places=5
    )  # The amount of the cryptocurrency held

    def __str__(self):
        return f"{self.user.full_name} - {self.cryptocurrency} - {self.amount}"


class StakingPool(models.Model):
    stak_holders = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="stacking_pools", blank=True
    )
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class PoolConditions(models.Model):
    pool = models.ForeignKey(StakingPool, on_delete=models.CASCADE)
    minimum_stake = models.DecimalField(max_digits=20, decimal_places=5)
    annual_percentage_yield = models.FloatField()

    def __str__(self):
        return f"{self.pool.name} - minimum stake - {self.minimum_stake}, annual percentage - {self.annual_percentage_yield}%"
