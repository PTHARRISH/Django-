from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
# @api view - convert a function into api view json drf response
from rest_framework.response import Response
from .models import User
from .serializer import User_serials
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
# @api_view(['PUT']) # "Hit by PUT method" when ever pass the put method before Method Not Allowed: /api/hit/
def hit(request):
    if request.method=="GET":
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
    elif request.method=="PUT":
        data=request.data # {"name":"Harrish"}
        print(data['name']) # Harrish
        print('You Hit a PUT Method')
        return Response("Hit by PUT method")

# Get api
# GET - when we get some data from the database get the method
# Method Not Allowed: /api/
# [31/Jan/2024 22:49:58] "GET /api/ HTTP/1.1" 405 5587
# This error message means that you are trying to use the GET method to access a view that does not support it. 
# The GET method is typically used to retrieve data from the server, 
# while the POST method is used to create or update data on the server
@api_view(['GET','POST'])
def get_post(request):
    if request.method=="GET":
        user_details=User.objects.all()
        serials=User_serials(user_details,many=True)
        return Response(serials.data) 
    elif request.method=="POST":
        data=request.data
        serials=User_serials(data=data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    
        

# CRUD using ID
@api_view(['GET','PUT','PATCH',"POST",'DELETE'])
def crud(request,id1):
    try:
        user_details=User.objects.get(id=id1)
    except User.DoesNotExist:
        return HttpResponse(id1+' is Not founded')
    if request.method=="GET":
        serials=User_serials(user_details)
        return Response(serials.data)
    elif request.method=="POST":
        data=request.data
        serials=User_serials(data=data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="PUT":
        data=request.data
        serials=User_serials(user_details,data=data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="PATCH":
        data=request.data
        serials=User_serials(user_details,data=data,partial=True)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="DELETE":
        user_details=User.objects.get(id=id1)
        user_details.delete()
        return HttpResponse(id1+' is Deleted')




# Postman CRUD 
        
@api_view(['GET','PUT','PATCH','DELETE','POST'])
def person(request):
    # try:
    #     data=request.data
    #     user_details=user.objects.get(id=data['id'])
    # except user.DoesNotExist:
    #     return HttpResponse(data[id]' is Not founded')
    if request.method=="GET":
        objs=User.objects.filter(color__isnull=False)
        # objs=User.objects.all()
        serials=User_serials(objs,many=True)
        return Response(serials.data)
    elif request.method=="POST":
        data=request.data
        serials=User_serials(data=data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="PUT":
        data=request.data
        objs=User.objects.get(id=data['id'])
        serials=User_serials(objs,data=data)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="PATCH":
        data=request.data
        objs=User.objects.get(id=data['id'])
        serials=User_serials(objs,data=data,partial=True)
        if serials.is_valid():
            serials.save()
            return Response(serials.data)
    elif request.method=="DELETE":
        data=request.data
        objs=User.objects.get(id=data['id'])
        objs.delete()
        return Response('Id is Deleted')


