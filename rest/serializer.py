from .models import user
from rest_framework import serializers

class user_serials(serializers.ModelSerializer):
    class Meta:
        model=user
        fields="__all__"

def validate(self, data):
        if 'age' in data:
            try:
                data['age'] = int(data['age'])
            except ValueError:
                raise serializers.ValidationError('Age must be an integer')
        return data