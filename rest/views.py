from django.shortcuts import render
from rest_framework.decorators import api_view
# @api view - convert a function into api view json drf response
from rest_framework.response import Response
# Create your views here.


# @api_view(['POST']) 
# if we use only post method it will display in api "detail": "Method \"GET\" not allowed."
@api_view(['GET'])
def index(request):
    course={
        'course_name':'Python',
        'frameworks':['flask','Django']
    }
    return Response(course)

@api_view(['GET','POST']) 
def index2(request):
    course={
        'course_name':'Python',
        'frameworks':['flask','Django']
    }
    return Response(course)

# @api_view(['GET']) # "Hit by GET method" printed
# @api_view(['POST']) # "Hit by POST method" when ever pass the post method before Method Not Allowed: /api/hit/
@api_view(['GET','POST']) # Method Not Allowed: /api/hit/ to avoid the error you need to pass GET method also in POST
def hit(request):
    if request.method=="GET":
        print(request.GET.get('search'))#search to display the name
        print('You Hit a GET Method')
        return Response("Hit by GET method")
    elif request.method=="POST":
        data=request.data
        #get the data 
        # from the postman and change the method to post and click raw and click plaintext to json 
        # type the data and click send
        print(data['name'])#get the data key
        print('You Hit a POST Method')
        return Response("Hit by POST method")

# Get api
# GET - when we get some data from the database get the method
# Method Not Allowed: /api/
# [31/Jan/2024 22:49:58] "GET /api/ HTTP/1.1" 405 5587
# This error message means that you are trying to use the GET method to access a view that does not support it. 
# The GET method is typically used to retrieve data from the server, 
# while the POST method is used to create or update data on the server
