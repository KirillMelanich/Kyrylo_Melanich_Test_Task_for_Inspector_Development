from django.contrib import admin

from .models import UserWallet, UserPosition, StakingPool, PoolConditions

admin.site.register(UserWallet)
admin.site.register(UserPosition)
admin.site.register(StakingPool)
admin.site.register(PoolConditions)
