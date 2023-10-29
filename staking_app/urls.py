from django.urls import path, include

from rest_framework import routers

from .views import (
    UserWalletViewSet,
    UserPositionViewSet,
    StackingPoolViewSet,
    PoolConditionsViewSet,
)

router = routers.DefaultRouter()
router.register("user_wallet", UserWalletViewSet)
router.register("user_position", UserPositionViewSet)
router.register("stacking_pool", StackingPoolViewSet)
router.register("pool_conditions", PoolConditionsViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "staking_app"
