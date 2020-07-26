from django.urls import path

from .views import ListUser,DetailUser,ListScenarioRole,DetailScenarioRole,ListScenario,DetailScenario,ListRoleItem,DetailRoleItem,ListRole,DetailRole,ListPastConsumptionItem,DetailPastConsumptionItem,ListPastConsumption,DetailPastConsumption,ListItem,DetailItem, SendAdminItem, UpdateUserItem,SendAdminQuantity,

urlpatterns = [
    path('user/', ListUser.as_view()),
    path('user/<int:pk>/', DetailUser.as_view()),

    path('scenariorole/', ListScenarioRole.as_view()),
    path('scenariorole/<int:pk>/', DetailScenarioRole.as_view()),

    path('scenario/', ListScenario.as_view()),
    path('scenario/<int:pk>/', DetailScenario.as_view()),

    path('roleitem/', ListRoleItem.as_view()),
    path('roleitem/<int:pk>/', DetailRoleItem.as_view()),

    path('role/', ListRole.as_view()),
    path('role/<int:pk>/', DetailRole.as_view()),

    path('pastconsumptionitem/', ListPastConsumptionItem.as_view()),
    path('pastconsumptionitem/<int:pk>/', DetailPastConsumptionItem.as_view()),

    path('pastconsumption/', ListPastConsumption.as_view()),
    path('pastconsumption/<int:pk>/', DetailPastConsumption.as_view()),

    path('item/', ListItem.as_view()),
    path('item/<int:pk>/', DetailItem.as_view()),

    path('roleitem/admin/', SendAdminItem),

    path('roleitem/updateuser', UpdateUserItem),
    
    #consumption log page
    path('pastc/admin/', SendAdminQuantity)
]
