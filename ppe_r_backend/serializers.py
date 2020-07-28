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

class RoleItemAdminSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.type')
    class Meta:
        fields = (
            'item_name',
            'quantity'
        )
        model = RoleItem

class UserItemGetSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.type')
    role_name = serializers.CharField(source='role.role_name')
    class Meta:
        fields = (
            'role_name'
            'item_name',
            'quantity'
        )
        model = RoleItem

# This needs editing as this serializer can not access role_name and item_name for a specific user, need to read into Nested Serializers, the views part is good.

class UserItemPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    scenario = serializers.CharField(source='scene_type')
    item_name = serializers.CharField(source='item.type')
    role_name = serializers.CharField(source='role.role_name')
    class Meta:
        fields = (
            'username',
            'scenario',
            'role_name',
            'item_name',
        )
        model = User
        
#consumption log page

#to get the itemwise sum of past-consumption of the roles given a scenario and date range
class PastConsScenarioAdminSerializer(serializers.ModelSerializer):
    # item_name = serializers.CharField(source='item.type')
    class Meta:
        fields = (
            # 'item_name',
            'quantity',
        )
        model = PastConsumptionItem
