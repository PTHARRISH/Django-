from django.shortcuts import render,redirect
from .forms import Userform
from .models import User

# Create your views here.
def display(request):
   m=User.objects.all() 
   return render(request,'display.html',{'form':m})

def add_data(request):
   if request.method=='POST':
    form=Userform(request.POST)
    if form.is_valid():
        form.save()
    return redirect('display/')
   elif request.method=='GET':
      form=Userform()
      return render(request,'add_data.html',{'form':form})
   
def update(request,pk):
   m=User.objects.get(id=pk)
   if request.method=='POST':
      form=Userform(request.POST,instance=m)
      if form.is_valid():
         form.save()
         return redirect('/display')
   else:
      form=Userform(instance=m)
      return render(request,'add_data.html',{'form':form})
   
def delete(request,pk):
   m=User.objects.get(id=pk)
   m.delete()
   return redirect("/display")