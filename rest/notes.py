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
