from rest_framework import generics

from .models import User
from .serializers import UserSerializer, UserSerializer, UserSerializer, UserSerializer, UserSerializer


class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer