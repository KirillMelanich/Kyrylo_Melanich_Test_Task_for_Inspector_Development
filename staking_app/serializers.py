from rest_framework import serializers

from .models import UserWallet, UserPosition, StakingPool, PoolConditions
from user.serializers import UserSerializer


class UserWalletSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = UserWallet
        fields = ("id", "user_id", "balance")


class UserWalletDetailSerializer(UserWalletSerializer):
    user = UserSerializer()

    class Meta:
        model = UserWallet
        fields = ("id", "balance", "user")


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = "__all__"


class UserPositionDetailSerializer(UserPositionSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = UserPosition
        fields = ("id", "cryptocurrency", "amount", "user")


class StakingPoolSerializer(serializers.ModelSerializer):
    stak_holders_number = serializers.SerializerMethodField()

    @staticmethod
    def get_stak_holders_number(obj):
        return obj.stak_holders.count()

    class Meta:
        model = StakingPool
        fields = ("id", "name", "description", "stak_holders_number", "created_at")


class StakingPoolDetailSerializer(StakingPoolSerializer):
    stak_holders = UserSerializer(read_only=True, many=True)

    class Meta:
        model = StakingPool
        fields = ("id", "name", "description", "stak_holders_number", "stak_holders", "created_at")


class PoolConditionsSerializer(serializers.ModelSerializer):
    pool_name = serializers.CharField(source="pool.name", read_only=True)

    class Meta:
        model = PoolConditions
        fields = ("id", "pool_name", "minimum_stake", "annual_percentage_yield")
