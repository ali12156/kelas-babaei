from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime as t
@api_view(["GET"])
def hello_havij(request):
    return(Response({"dalam":str(t.datetime.now())}))
# Create your views here.
