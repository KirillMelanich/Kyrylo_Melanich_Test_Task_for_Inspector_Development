from django.urls import path, include

from rest_framework import routers

from .views import (
    UserWalletViewSet,
    UserPositionViewSet,
    StackingPoolViewSet,
    PoolConditionsViewSet,
)

router = routers.DefaultRouter()
router.register("user_wallet", UserWalletViewSet, basename="user_wallet")
router.register("user_position", UserPositionViewSet, basename="user_position")
router.register("staking_pool", StackingPoolViewSet, basename="staking_pool")
router.register("pool_conditions", PoolConditionsViewSet, basename="pool_conditions")

urlpatterns = [path("", include(router.urls))]

app_name = "staking_app"
