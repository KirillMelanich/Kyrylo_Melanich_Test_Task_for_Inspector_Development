from rest_framework import viewsets

from .models import UserWallet, UserPosition, StackingPool, PoolConditions
from .serializers import (
    UserWalletSerializer,
    UserPositionSerializer,
    StackingPoolSerializer,
    StackingPoolDetailSerializer,
    PoolConditionsSerializer,
)


class UserWalletViewSet(viewsets.ModelViewSet):
    queryset = UserWallet.objects.all()
    serializer_class = UserWalletSerializer


class UserPositionViewSet(viewsets.ModelViewSet):
    queryset = UserPosition.objects.all()
    serializer_class = UserPositionSerializer


class StackingPoolViewSet(viewsets.ModelViewSet):
    queryset = StackingPool.objects.all().prefetch_related("stack_holders")
    serializer_class = StackingPoolSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StackingPoolDetailSerializer
        return StackingPoolSerializer


class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer
