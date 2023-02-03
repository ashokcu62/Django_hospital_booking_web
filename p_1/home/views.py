from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments, Doctors
from .form import BookingForm

# Create your views here.


def index(request):
    return render(request, 'index.html',)


def about(request):
    return render(request, "about.html")


def doctors(request):
    dict_doc = {
        'doc': Doctors.objects.all
    }
    return render(request, "doctors.html", dict_doc)


def booking(request):
    # print("booking req ", request.method)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html',)


    form = BookingForm()
    dict_form = {
        "form": form
    }
    print("for is "*12)
    print(dict_form)
    return render(request, "booking.html", dict_form)


def contact(request):
    return render(request, 'contact.html')


def department(request):
    dict_dept = {
        'dept': Departments.objects.all

    }
    return render(request, 'department.html', dict_dept)

