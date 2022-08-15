from django.shortcuts import render
from django.http import HttpResponse
from django import template
from rest_framework.response import Response
from rest_framework.decorators import api_view

 # Create your views here.


def index(request):

    return render(request, "electrical/index.html")

def voltage(request):

    return render(request, "electrical/voltage.html")

def calc(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a*b
    return render(request, "electrical/voltage.html", {'calc_value': 'my power in volts is ' +str(c)})

def amps(request):

    return render(request, "electrical/amps.html")

def avr(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a/b
    return render(request, "electrical/amps.html", {'avr_value': 'my current in amperage is ' +str(c)})

def res(request):

    return render(request, "electrical/resistance.html")

def rva(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a/b
  
    return render(request, "electrical/resistance.html", {'rva_value': 'my resistance in ohms is ' +str(c)})

def meff(request):

    return render(request, "electrical/meff.html")

def eff(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a/b
  
    return render(request, "electrical/meff.html", {'eff_value': 'my efficiency is ' +str(c)})

def watt(request):

    return render(request, "electrical/watt.html")

def wat(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=a*b
  
    return render(request, "electrical/watt.html", {'wat_value': 'my true power in wattage is ' +str(c)})

def pfr(request):

    return render(request, "electrical/pfr.html")

def pf(request):
    a=float(request.GET['t1'])
    b=float(request.GET['t2'])
    c=(a/b) * 100

    return render(request, "electrical/pfr.html", {'pf_value': 'my power factor is ' +str(c)})

def hp(request):

    return render(request, "electrical/hp.html")

def hpw(request):
    a=float(request.GET['t1'])
    
    c=a*746

    return render(request, "electrical/hp.html", {'hpw_value': 'my wattage is ' +str(c)})


