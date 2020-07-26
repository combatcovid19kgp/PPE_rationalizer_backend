from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,ScenarioRole,Scenario,RoleItem,Role,PastConsumptionItem,PastConsumption,Item
from .serializers import UserSerializer, ScenarioSerializer, RoleSerializer, RoleItemSerializer, ScenarioRoleSerializer,ItemSerializer,PastConsumptionSerializer,PastConsumptionItemSerializer, RoleItemAdminSerializer, UserItemGetSerializer, UserItemPostSerializer , PastConsScenarioAdminSerializer

#User
class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



#ScenarioRole
class ListScenarioRole(generics.ListCreateAPIView):
    queryset = ScenarioRole.objects.all()
    serializer_class = ScenarioRoleSerializer


class DetailScenarioRole(generics.RetrieveUpdateDestroyAPIView):
    queryset = ScenarioRole.objects.all()
    serializer_class = ScenarioRoleSerializer



#Scenario
class ListScenario(generics.ListCreateAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer


class DetailScenario(generics.RetrieveUpdateDestroyAPIView):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer



#RoleItem
class ListRoleItem(generics.ListCreateAPIView):
    queryset = RoleItem.objects.all()
    serializer_class = RoleItemSerializer


class DetailRoleItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleItem.objects.all()
    serializer_class = RoleItemSerializer



#Role
class ListRole(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class DetailRole(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



#PastConsumptionItem
class ListPastConsumptionItem(generics.ListCreateAPIView):
    queryset = PastConsumptionItem.objects.all()
    serializer_class = PastConsumptionItemSerializer


class DetailPastConsumptionItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastConsumptionItem.objects.all()
    serializer_class = PastConsumptionItemSerializer



#PastConsumption
class ListPastConsumption(generics.ListCreateAPIView):
    queryset = PastConsumption.objects.all()
    serializer_class = PastConsumptionSerializer


class DetailPastConsumption(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastConsumption.objects.all()
    serializer_class = PastConsumptionSerializer



#Item
class ListItem(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DetailItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

@api_view(['GET'])
def SendAdminItem(request):
    if request.method=='GET':
        scene=request.query_params['scenario']
        role=request.query_params['role']
        scenario_id = Scenario.objects.filter(user=3, scene_type=scene).values_list('scenario_id', flat=True)[0]
        role_id = Role.objects.filter(role_name= role).values_list('role_id', flat=True)[0]
        data = RoleItem.objects.filter(scenario = scenario_id, role= role_id)
        serializer = RoleItemAdminSerializer(data ,many=True)
        return Response(serializer.data)

@api_view(['GET','POST','PUT'])
def UpdateUserItem(request):
    if request.method=='GET':
        username=request.query_params['username']
        scene=request.query_params['scenario']
        scenario_id = Scenario.objects.filter(user=username, scene_type=scene).values_list('scenario_id', flat=True)[0]
        user_id = User.objects.filter(username=username).values_list('user_id', flat=True)[0]
        data = RoleItem.objects.filter(user=user_id, scenario = scenario_id)
        serializer = UserItemGetSerializer(data, many= True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer = UserItemPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=='PUT':
        serializer = UserItemPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
#consumption log -- Needs Correction :(
#to get the itemwise sum of past-consumption of the roles given a scenario and date range
@api_view(['GET'])
def SendAdminQuantity(request):
    if request.method=='GET':
        scene = request.query_params['scenario']
        date_range = request.query_params['date']
        
        scenario_id = Scenario.objects.filter(user=3, scene_type=scene).values_list('scenario_id', flat=True)[0]
        consumption_id = PastConsumption.objects.filter(date=date_range, scenario=scenario_id).values_list('consumption_id', flat=True)[0]
       
        data = PastConsumptionItem.objects.filter(consumption_id=consumption_id)
        serializer = PastConsScenarioAdminSerializer(data ,many=True)
        return Response(serializer.data)
