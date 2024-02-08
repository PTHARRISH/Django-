from .models import user
from rest_framework import serializers

class user_serials(serializers.ModelSerializer):
    class Meta:
        model=user
        fields="__all__"

    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        return data