from rest_framework import serializers

from .models import UserWallet, UserPosition, StackingPool, PoolConditions
from user.serializers import UserSerializer


class UserWalletSerializer(serializers.ModelSerializer):
    wallet_holder_name = serializers.CharField(source="user.full_name", read_only=True)
    wallet_holder_id = serializers.CharField(source="user.id", read_only=True)

    class Meta:
        model = UserWallet
        fields = ("id", "wallet_holder_id", "balance", "wallet_holder_name")


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = "__all__"


class StackingPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = StackingPool
        fields = ("id", "name", "description", "stack_holders", "created_at")


class StackingPoolDetailSerializer(StackingPoolSerializer):
    stack_holders = UserSerializer(read_only=True, many=True)


class PoolConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoolConditions
        fields = "__all__"
