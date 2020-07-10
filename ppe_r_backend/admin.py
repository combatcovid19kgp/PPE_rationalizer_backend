from django.contrib import admin

# Register your models here.

from .models import User, Scenario, ScenarioRole, Role, RoleItem, Item, PastConsumptionItem, PastConsumption

admin.site.register(User)
admin.site.register(Scenario)
admin.site.register(ScenarioRole)
admin.site.register(Role)
admin.site.register(RoleItem)
admin.site.register(Item)
admin.site.register(PastConsumptionItem)
admin.site.register(PastConsumption)