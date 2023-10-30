from rest_framework import serializers

from .models import UserWallet, UserPosition, StakingPool, PoolConditions
from user.serializers import UserSerializer, UserCardSerializer


class UserWalletSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = UserWallet
        fields = ("id", "user_id", "balance")

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user

        # Check if the user already has a wallet
        if UserWallet.objects.filter(user=user).exists():
            raise serializers.ValidationError("User already has a wallet.")

        # Extract the 'balance' data from validated_data
        balance = validated_data.pop("balance", None)

        # Create the UserWallet instance
        user_wallet = UserWallet.objects.create(user=user, balance=balance)
        return user_wallet


class UserWalletDetailSerializer(serializers.ModelSerializer):
    user = UserCardSerializer(read_only=True)

    class Meta:
        model = UserWallet
        fields = ("id", "balance", "user")


class UserPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosition
        fields = ("id", "cryptocurrency", "amount", "user")
        read_only_fields = ("user",)


class UserPositionDetailSerializer(UserPositionSerializer):
    user = UserCardSerializer(read_only=True, many=False)

    class Meta:
        model = UserPosition
        fields = ("id", "cryptocurrency", "amount", "user")


class StakingPoolSerializer(serializers.ModelSerializer):
    number_of_stack_holders = serializers.SerializerMethodField()

    @staticmethod
    def get_number_of_stack_holders(obj):
        return obj.stak_holders.count()

    class Meta:
        model = StakingPool
        fields = ("id", "name", "description", "number_of_stack_holders", "created_at")


class StakingPoolDetailSerializer(StakingPoolSerializer):
    stak_holders = UserSerializer(many=True, read_only=False)

    class Meta:
        model = StakingPool
        fields = (
            "id",
            "name",
            "description",
            "number_of_stack_holders",
            "stak_holders",
            "created_at",
        )


class PoolConditionsSerializer(serializers.ModelSerializer):
    pool_name = serializers.CharField(source="pool.name", read_only=True)

    class Meta:
        model = PoolConditions
        fields = ("id", "pool_name", "minimum_stake", "annual_percentage_yield")
