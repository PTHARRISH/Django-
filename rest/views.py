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

@api_view(['GET','POST','PUT']) 
def index2(request):
    course={
        'course_name':'Python',
        'frameworks':['flask','Django']
    }
    return Response(course)

# Get api
# GET - when we get some data from the database get the method
# Method Not Allowed: /api/
# [31/Jan/2024 22:49:58] "GET /api/ HTTP/1.1" 405 5587
# This error message means that you are trying to use the GET method to access a view that does not support it. 
# The GET method is typically used to retrieve data from the server, 
# while the POST method is used to create or update data on the server
