from rest_framework import viewsets

from .models import UserWallet, UserPosition, StakingPool, PoolConditions
from .permissions import IsAdminOrIfAuthentificatedReadOnly
from .serializers import (
    UserWalletSerializer,
    UserPositionSerializer,
    StakingPoolSerializer,
    StakingPoolDetailSerializer,
    PoolConditionsSerializer, UserWalletDetailSerializer, UserPositionDetailSerializer,
)


class UserWalletViewSet(viewsets.ModelViewSet):
    queryset = UserWallet.objects.all()
    serializer_class = UserWalletSerializer
    permission_classes = (IsAdminOrIfAuthentificatedReadOnly, )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserWalletDetailSerializer
        return UserWalletSerializer


class UserPositionViewSet(viewsets.ModelViewSet):
    queryset = UserPosition.objects.all().select_related("user")
    serializer_class = UserPositionSerializer
    permission_classes = (IsAdminOrIfAuthentificatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserPositionDetailSerializer
        return UserPositionSerializer


class StackingPoolViewSet(viewsets.ModelViewSet):
    queryset = StakingPool.objects.all().prefetch_related("stak_holders")
    serializer_class = StakingPoolSerializer
    permission_classes = (IsAdminOrIfAuthentificatedReadOnly,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StakingPoolDetailSerializer
        return StakingPoolSerializer


class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer
