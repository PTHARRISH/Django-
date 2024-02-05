from django.urls import path
from . import views

urlpatterns = [
    path('display/',views.display ),
    path('',views.add_data ),
    path('update/<pk>',views.update ),
    path('delete/<pk>',views.delete ),
]
