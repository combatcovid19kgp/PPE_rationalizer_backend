from rest_framework import serializers
from .models import User


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