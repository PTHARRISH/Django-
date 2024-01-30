from django.shortcuts import render,redirect
from .forms import Userform
from .models import User

# Create your views here.
def display(request):
   if request.method=='POST':
      pass
      
   return render(request,'display.html',{})

def add_data(request):
   if request.method=='POST':
    form=Userform(request.POST)
    if form.is_valid():
        form.save()
    return redirect('display/')
   elif request.method=='GET':
      form=Userform()
      return render(request,'add_data.html',{'form':form})

