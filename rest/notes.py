# serializer -
# serializer is a concept that converts a query set into json format and viceversa
# and save a data into database is called deserializer.
# class which helps you to serialize the data in the form queryset to json response and viceversa.

# most use serializer is model view serializer 

# @api_view:
# @api_view(['GET']) # "Hit by GET method" printed
# @api_view(['POST']) # "Hit by POST method" when ever pass the post method before Method Not Allowed: /api/hit/
# @api_view(['GET','POST']) # Method Not Allowed: /api/hit/ to avoid the error you need to pass GET method also in POST
# @api_view(['PUT']) # like the POST "Hit by PUT method" when ever pass the put method before Method Not Allowed: /api/hit/



# Get api
# GET - when we get some data from the database get the method
# Method Not Allowed: /api/
# [31/Jan/2024 22:49:58] "GET /api/ HTTP/1.1" 405 5587
# This error message means that you are trying to use the GET method to access a view that does not support it. 
# The GET method is typically used to retrieve data from the server, 
# while the POST method is used to create or update data on the server




# Model
# Create a class color and add the field color name on it and create a color field in user class  
# Color class
# color_name=models.CharField(max_length=100)

# User class
# color=models.ForeignKey(Color,null=True,blank=True,on_delete=models.CASCADE) 

# null and blank is true because we already created data after now add new field it show some error
# to avoid the error and we will add null and blank true it will all the previous color field is allotted True

# After enter the admin to add colors table and User to connect the color fields

# {
#         "id": 7,
#         "name": "Harrish",
#         "user": "admin",
#         "password": "123",
#         "color": 1
#     },
#     {
#         "id": 8,
#         "name": "admin",
#         "user": "harrishpt@gmail.com",
#         "password": "Admin@123",
#         "color": 3
#     }
# ]
# 
# now the color will show numbers color:3, color:1 colors numbers on it

# It can be any color so identify its color

# objs=User.objects.filter(color__isnull=False)

#  it will print except null presented fields 
# [
#     {
#         "id": 7,
#         "name": "Harrish",
#         "user": "admin",
#         "password": "123",
#         "color": 1
#     },
#     {
#         "id": 8,
#         "name": "admin",
#         "user": "harrishpt@gmail.com",
#         "password": "Admin@123",
#         "color": 3
#     },
#     {
#         "id": 9,
#         "name": "Harrish",
#         "user": "admin",
#         "password": "123",
#         "color": 3
#     },
#     {
#         "id": 10,
#         "name": "admin",
#         "user": "admin",
#         "password": "123",
#         "color": 2
#     }
# ]

# we don't know what is 1,2 and 3 represent
# so we need to add serializer inside 

# depth=1 (get all the keys from the foreign key model)
# the  depth keyword display the connected foreign keys Id and its Color_name fields also

#  {
#         "id": 7,
#         "name": "Harrish",
#         "user": "admin",
#         "password": "123",
#         "color": {
#             "id": 1,
#             "color_name": "Green"
#         }
#   }

# Instead of we using the depth=1 we create the color serializer and call the the user to call it
# class User_serials(serializers.ModelSerializer):
#   color=Color_serials()

# Now we use this serializer and call the color serializer to get the color_name and print its color on it.

# method serializer fields in django method
# Instead OF Adding country fields directly into the model fields   
# create the method serializer
# If you use Serializermethod you need to create the method name (get_methodserializerfieldname) 

# In color_code method
# We call the object and we geth obj=current object("id": 1),(color.id is color class id to call the color id ).
# color_oj is store id colors fields


#  when you want to write all the functionality custom then we use this serializer

# # Error :AssertionError at /api/person/
# The `.create()` method does not support writable nested fields by default.
# Write an explicit `.create()` method for serializer `rest.serializer.User_serials`, or set `read_only=True` on nested serializer fields.
# To create a nested serializer, you need to do two things:

# Define the nested serializer class, such as ProfileSerializer, and specify its model and fields.
# Use the nested serializer class as a field in the parent serializer class, such as UserSerializer, 
# and specify the source attribute to indicate the related model field.
# For example, if you have a User model that has a one-to-one relation with a Profile model, 
# you can define the serializers 