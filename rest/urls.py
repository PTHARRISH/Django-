from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index ),# GET - http://127.0.0.1:8000/api/ display the courses .HTTP 405 Method Not Allowed
    path('index2/',views.index2 ),
    path('hit/',views.hit ),
    path("get/",views.get_post),
    path("crud/<id1>",views.crud),
    path("person/",views.person),
    
]
