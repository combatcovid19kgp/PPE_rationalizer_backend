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

class RoleItemIntermediateSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.type')
    item_quantity = serializers.CharField(source='quantity')
    class Meta:
        model = RoleItem
        fields = ('item_name', 'item_quantity')

class RoleItemFinalSerializer(serializers.ModelSerializer):
    itemquan = serializers.SerializerMethodField()
    role_name = serializers.CharField(source='role.role_name')
    role_quantity = serializers.CharField(source='quantity')
    class Meta:
        model = ScenarioRole
        fields = ('role_name', 'role_quantity','itemquan')

    def get_itemquan(self, obj):
        scenario_id=obj.scenario
        role_id=obj.role
        qset = RoleItem.objects.filter(scenario=scenario_id,role=role_id)
        return [RoleItemIntermediateSerializer(m).data for m in qset]


class RoleItemPostPutSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    scenario = serializers.CharField(source='scene_type')
    roleitem = RoleItemFinalSerializer(many=True)
    class Meta:
        model = Scenario
        fields = ('username','scenario','roleitem')

    # def create(self, validated_data):

    # def update(self, instance, validated_data):

# class UpdateDemandSerializer(serializers.ModelSerializer):


#consumption log page

#to get the itemwise sum of past-consumption of the roles given a scenario and date range
class PastConsScenarioAdminSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.type')
    class Meta:
        fields = (
             'item_name',
            'quantity',
        )
        model = PastConsumptionItem

#to get the itemwise sum of past-consumption of the roles given a date range(for all scenarios)
class PastConsOverallAdminSerializer(serializers.ModelSerializer):
    item_name = serializers.CharField(source='item.type')
    class Meta:
        fields = (
             'item_name',
            'quantity',
        )
        model = PastConsumptionItem