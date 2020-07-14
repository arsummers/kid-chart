from django.contrib import admin
from .models import Kids, KidInstance, Reward, Rules, RuleInstance

@admin.register(Kids)
class KidAdmin(admin.ModelAdmin):
    pass

@admin.register(KidInstance)
class KidInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

@admin.register(Rules)
class RuleAdmin(admin.ModelAdmin):
    pass

@admin.register(RuleInstance)
class RuleInstanceAdmin(admin.ModelAdmin):
    pass