from rest_framework import serializers
from .models import User, Scenario, Role, Item, PastConsumption, ScenarioRole, RoleItem, PastConsumptionItem


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'user_id',
            'org_name',
            'username',
            'email',
            'pincode',
            'state',
            'mobile'
        )
        model = User

class ScenarioSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'scene_type',
            'user',
            'scenario_id'
        )
        model = Scenario

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'role_name',
            'role_id'
        )
        model = Role

class ScenarioRoleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'quantity',
            'role',
            'scenario'
        )
        model = ScenarioRole

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'type',
            'item_id'
        )
        model = Item

class RoleItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'quantity',
            'cost_piece',
            'scenario',
            'role',
            'item'
        )
        model = RoleItem

class PastConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'date',
            'scenario',
            'role',
            'consumption_id'
        )
        model = PastConsumption


class PastConsumptionItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'quantity',
            'consumption',
            'item'
        )
        model = PastConsumptionItem
