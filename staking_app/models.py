from django.conf import settings
from django.db import models
from rest_framework import serializers


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

    def save(self, *args, **kwargs):
        """
        This method makes impossible to create UserPosition instance
        if sum of all UserPosition amounts will be bigger than User's balance
        """
        user_wallet = UserWallet.objects.get(user=self.user)
        total_amount = (
            UserPosition.objects.filter(user=self.user).aggregate(
                total_amount=models.Sum("amount")
            )["total_amount"]
            or 0
        )

        if total_amount + self.amount > user_wallet.balance:
            difference = (total_amount + self.amount) - user_wallet.balance
            raise serializers.ValidationError(
                f"The total amount of the user's positions"
                f" cannot exceed his wallet balance ({user_wallet.balance})."
                f" The additional amount would exceed the balance by {difference}."
                f" Please set up amount not bigger than {user_wallet.balance - total_amount} ",
                code="invalid",
            )

        super().save(*args, **kwargs)


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
        return (
            f"{self.pool.name} - minimum stake - {self.minimum_stake},"
            f" annual percentage - {self.annual_percentage_yield}%"
        )
