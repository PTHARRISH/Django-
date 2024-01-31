from django.shortcuts import render
from rest_framework.decorators import api_view
# @api view - convert a function into api view json drf response
from rest_framework.response import Response
# Create your views here.


@api_view(['GET'])
def index(request):
    course={
        'course_name':'Python',
        'frameworks':['flask','Django']
    }
    return Response(course)

# Get api
# GET - when we get some data from the database get the method
# @api_view(['GET','POST'])
# def 
