from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments

# Create your views here.
def index(request):
   numbers={
    "num1":[1,2,3,4,5,6,7,8,9,10]
   }
   return render(request,'index.html',numbers)

def about(request):
    return render(request,"about.html")

def doctors(request):
    return render(request,"doctors.html")

def booking(request):
    return render(request,"booking.html")

def contact(request):
    return render(request,'contact.html')

def department(request):
    dict_dept={
        'dept':Departments.objects.all
        
    }
    return render(request,'department.html',dict_dept)

