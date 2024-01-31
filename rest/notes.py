# serializer -
# serializer is a concept that converts a query set into json format and viceversa
# and save a data into database is called deserializer.
# class which helps you to serialize the data in the form queryset to json response and viceversa.

# most use serializer is model view serializer 

# @api_view:
# @api_view(['GET']) # "Hit by GET method" printed
# @api_view(['POST']) # "Hit by POST method" when ever pass the post method before Method Not Allowed: /api/hit/
# @api_view(['GET','POST']) # Method Not Allowed: /api/hit/ to avoid the error you need to pass GET method also in POST
