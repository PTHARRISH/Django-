from .models import user
from rest_framework import serializers

class user_serials(serializers.ModelSerializer):
    class Meta:
        model=user
        fields="__all__"