from django.urls import path , include
from . import views

urlpatterns = [
    path("",views.index),
    path("about/",views.about),
    path("doctors/",views.doctors),
    path("booking/",views.booking),
    path("contact/",views.contact),
    path("department/",views.department)

]
