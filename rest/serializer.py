from .models import User
from rest_framework import serializers


class User_serials(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"



