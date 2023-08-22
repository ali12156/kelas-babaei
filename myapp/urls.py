from django.urls import path
from myapp import views

urlpatterns = [
    path("data",views.hello_havij)
]