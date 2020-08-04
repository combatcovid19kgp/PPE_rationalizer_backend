from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,ScenarioRole,Scenario,RoleItem,Role,PastConsumptionItem,PastConsumption,Item
from .serializers import UserSerializer, ScenarioSerializer, RoleSerializer, RoleItemSerializer, ScenarioRoleSerializer,ItemSerializer,PastConsumptionSerializer,PastConsumptionItemSerializer, RoleItemAdminSerializer, RoleItemPostPutSerializer, RoleItemGetSerializer, RoleItemGetFinalSerializer, ScenarioRoleDeleteSerializer, RoleItemDeleteSerializer, RoleItemGetOverallSerializer, PastConsScenarioAdminSerializer ,PastConsOverallAdminSerializer
from datetime import datetime

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

@api_view(['GET','POST'])
def UpdateUserItem(request):

    if request.method=='GET':
        userna=request.query_params['username']
        scene=request.query_params['scenario']
        user_id = User.objects.filter(username=userna).values_list('user_id', flat=True)[0]
        scenario_id = Scenario.objects.filter(user=user_id, scene_type=scene).values_list('scenario_id', flat=True)[0]
        data = Scenario.objects.filter(scenario_id = scenario_id)
        serializer = RoleItemGetFinalSerializer(data[0])
        return Response(serializer.data)
        
    elif request.method=='POST':
        serializer = RoleItemPostPutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors)

@api_view(['GET'])
def OverallUserItem(request):

    if request.method=='GET':
        userna=request.query_params['username']
        user_id = User.objects.filter(username=userna).values_list('user_id', flat=True)[0]
        data = Scenario.objects.filter(user=user_id)
        serializer = RoleItemGetOverallSerializer(data, many=True)
        return Response(serializer.data)

@api_view(['DELETE'])
def DeleteUserRole(request):
    if request.method=='DELETE':
        serializer = ScenarioRoleDeleteSerializer(data = request.data)
        if serializer.is_valid():
            request_data=serializer.data
            userna=request_data['username']
            scene=request_data['scenario']
            user_id = User.objects.filter(username=userna).values_list('user_id', flat=True)[0]
            scenario_id = Scenario.objects.filter(user=user_id, scene_type=scene).values_list('scenario_id', flat=True)[0]
            role=request_data['role']
            role_id = Role.objects.filter(role_name=role).values_list('role_id', flat=True)[0]
            data = ScenarioRole.objects.filter(role=role_id, scenario=scenario_id)[0]
            data.delete()
            return Response('Role Deleted')

@api_view(['DELETE'])
def DeleteUserItem(request):
    if request.method=='DELETE':
        serializer = RoleItemDeleteSerializer(data = request.data)
        if serializer.is_valid():
            request_data=serializer.data
            userna=request_data['username']
            scene=request_data['scenario']
            user_id = User.objects.filter(username=userna).values_list('user_id', flat=True)[0]
            scenario_id = Scenario.objects.filter(user=user_id, scene_type=scene).values_list('scenario_id', flat=True)[0]
            role=request_data['role']
            role_id = Role.objects.filter(role_name=role).values_list('role_id', flat=True)[0]
            item=request_data['item']
            item_id = Item.objects.filter(type=item).values_list('item_id', flat=True)[0]
            data = RoleItem.objects.filter(role=role_id, scenario=scenario_id, item=item_id)[0]
            data.delete()
            return Response('Item Deleted')

#to get the itemwise sum of past-consumption of the roles given a scenario and date range
@api_view(['GET'])
def SendAdminQuantity(request):
    if request.method=='GET':
        scene = request.query_params['scenario']
        date1 = request.query_params['datestart']
        date2 = request.query_params['dateend']
     
        #taking the values of all available dates in array 'dates'
        dates = []
        qsd=PastConsumption.objects.all()
        qsd=qsd.values(*dates)

        #taking dates as input in array 'dater' with 2 elements
        dater = [datetime.strptime(date1, '%Y-%m-%d').date(),datetime.strptime(date2, '%Y-%m-%d').date()]

    
        scenario_id = Scenario.objects.filter(user=1, scene_type=scene).values_list('scenario_id', flat=True)[0]
        consid = []
        qs=PastConsumption.objects.all()
        qs=qs.filter(date__range=[dater[0],dater[1]] ,scenario=scenario_id)
        qs=qs.values(*consid)
        
        data_id= []
        for elem in qs:
            data_id.append(PastConsumptionItem.objects.filter(consumption_id=elem['consumption_id']).values_list('consumption_id', flat=True)[0])

        data = PastConsumptionItem.objects.filter(pk__in=data_id)

        
        
        serializer = PastConsScenarioAdminSerializer(data ,many=True)
        return Response(serializer.data)


#overall tab
@api_view(['GET'])
def SendAdminQuantoverall(request):
    if request.method=='GET':
        
        date1 = request.query_params['datestart']
        date2 = request.query_params['dateend']
     
        #taking the values of all available dates in array 'dates'
        dates = []
        qsd=PastConsumption.objects.all()
        qsd=qsd.values(*dates)

        #taking dates as input in array 'dater' with 2 elements
        dater = [datetime.strptime(date1, '%Y-%m-%d').date(),datetime.strptime(date2, '%Y-%m-%d').date()]

    
        consid = []
        qs=PastConsumption.objects.all()
        qs=qs.filter(date__range=[dater[0],dater[1]])
        qs=qs.values(*consid)
        
        data_id= []
        for elem in qs:
            data_id.append(PastConsumptionItem.objects.filter(consumption_id=elem['consumption_id']).values_list('consumption_id', flat=True)[0])

        data = PastConsumptionItem.objects.filter(pk__in=data_id)

        
        
        serializer = PastConsOverallAdminSerializer(data ,many=True)
        return Response(serializer.data)
