from django.shortcuts import render
from django.http import HttpResponse
from django import template
from rest_framework.response import Response
from rest_framework.decorators import api_view

 # Create your views here.


def index(request):
    return render(request, "electrical/index.html")

def calc(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a*b
    return render(request, "electrical/index.html", {'calc_value': 'my output is ' +str(c)})
