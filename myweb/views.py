#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request,"myweb/index.html")
def education(request):
    return render(request,"myweb/education.html")
def career(request):
    return render(request,"myweb/career.html")
def contact_us(request):
    return render(request,"myweb/contactus.html")  
def about(request):
    return render(request,"myweb/about.html")  