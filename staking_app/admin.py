from django.contrib import admin

from .models import UserWallet, UserPosition, StackingPool, PoolConditions

admin.site.register(UserWallet)
admin.site.register(UserPosition)
admin.site.register(StackingPool)
admin.site.register(PoolConditions)
