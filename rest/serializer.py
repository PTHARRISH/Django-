from .models import User,Color
from rest_framework import serializers

class Color_serials(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=["color_name"]



class User_serials(serializers.ModelSerializer):
    color=Color_serials()
    class Meta:
        model = User
        fields = "__all__"
        # depth=1



