from django.urls import path
from . import views

urlpatterns = [
    path("calculator", views.index, name="index"),
    path("volts", views.voltage, name="voltage"),
    path("calc", views.calc, name="volts"),
    path("amps", views.amps, name="amperage"),
    path("avr", views.avr, name="amps"),
    path("res", views.res, name="resistance"),
    path("rva", views.rva, name="ohms"),
    path("meff", views.meff, name="motor efficiency"),
    path("eff", views.eff, name="eff"),
    path("watt", views.watt, name="true power"),
    path("wat", views.wat, name="wat"),
    path("pfr", views.pfr, name="power factor"),
    path("pf", views.pf, name="pf"),
    path("hp", views.hp, name="hp"),
    path("hpw", views.hpw, name="hpw")
]


