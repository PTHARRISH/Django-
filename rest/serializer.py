from .models import User,Color
from rest_framework import serializers

class Color_serials(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=["color_name","id"]



class User_serials(serializers.ModelSerializer):
    color=Color_serials()
    class Meta:
        model = User
        fields = "__all__"
        # depth=1

    def validate(self,data):
        special_chars="!@#$%^&*()_+=-|\":><?/.,;'][{|}]"
        if any (c in special_chars for c in data["name"]):
            raise serializers.ValidationError('Name cannot contain Special Characters')



