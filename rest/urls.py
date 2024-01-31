from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ),# GET - http://127.0.0.1:8000/api/ display the courses .HTTP 405 Method Not Allowed
    path('index/',views.index2 ),
]
