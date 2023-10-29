from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import UserWallet, UserPosition, StakingPool, PoolConditions
from .permissions import IsOwnerOrAdminUser
from .serializers import (
    UserWalletSerializer,
    UserPositionSerializer,
    StakingPoolSerializer,
    StakingPoolDetailSerializer,
    PoolConditionsSerializer,
    UserWalletDetailSerializer,
    UserPositionDetailSerializer,
)


class UserWalletViewSet(viewsets.ModelViewSet):
    queryset = UserWallet.objects.all()
    serializer_class = UserWalletSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrAdminUser,
    )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserWalletDetailSerializer
        return UserWalletSerializer

    def create(self, request, *args, **kwargs):
        """
        This method allows an authorized user to create only one wallet and only for himself.
        """
        if UserWallet.objects.filter(user=request.user).exists():
            return Response(
                {
                    "message": "One user can have only one wallet.You already have a wallet"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = UserWalletSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPositionViewSet(viewsets.ModelViewSet):
    queryset = UserPosition.objects.all().select_related("user")
    serializer_class = UserPositionSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrAdminUser,
    )

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserPositionDetailSerializer
        return UserPositionSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StackingPoolViewSet(viewsets.ModelViewSet):
    queryset = StakingPool.objects.all().prefetch_related("stak_holders")
    serializer_class = StakingPoolSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == "retrieve":
            return StakingPoolDetailSerializer
        return StakingPoolSerializer


class PoolConditionsViewSet(viewsets.ModelViewSet):
    queryset = PoolConditions.objects.all()
    serializer_class = PoolConditionsSerializer
    permission_classes = (IsAuthenticated,)
