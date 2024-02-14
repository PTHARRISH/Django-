from .models import User,Color
from rest_framework import serializers

# color class
class Color_serials(serializers.ModelSerializer):
    class Meta:
        model=Color
        fields=["color_name","id"] # display fields in as mentioned in dictionary in user serials



class User_serials(serializers.ModelSerializer):
    # after creating color class you need to mention and call the object.
    color=Color_serials()

    # method serializer
    color_code =serializers.SerializerMethodField() 
    pin=serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"
        #  after creating the colors now it will shows color:1
        #  don't need to create color class after depth keyword display all the fields in the color class
        # depth=1 # 
        # color class created

    # If you use Serializermethod you need to create the method name (get_methodserializerfieldname) 
    def get_color_code(self,obj):
        print(obj.color.id)
        color_obj=Color.objects.get(id=obj.color.id) 
        # here obj=current object("id": 1),(color.id is color class id to call the color id ).
        # color_oj is store id colors fields
        print(color_obj)
        return {'color_name':color_obj.color_name,'hexa_code':"#000"}
    
    def get_pin(self,obj):
        return "svk"

    def validate(self,data):
        special_chars="!@#$%^&*()_+=-|\":><?/.,;'][{|}]"
        if any (c in special_chars for c in data["name"]):
            raise serializers.ValidationError('Name cannot contain Special Characters')



