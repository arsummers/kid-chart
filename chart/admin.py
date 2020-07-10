from django.contrib import admin
from .models import Kid, KidInstance, Reward, Rule

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    pass

@admin.register(KidInstance)
class KidInstanceAdmin(admin.ModelAdmin):
    pass

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass