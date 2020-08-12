from django.contrib import admin
from .models import Kid, KidInstance, Reward, Rule

@admin.register(Kid)
class KidAdmin(admin.ModelAdmin):
    pass

@admin.register(KidInstance)
class KidInstanceAdmin(admin.ModelAdmin):
    list_display = ('kid', 'points', 'parent', 'id')

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    pass

@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    pass

# @admin.register(RuleInstance)
# class RuleInstanceAdmin(admin.ModelAdmin):
#     pass