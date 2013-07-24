# Create your views here.
#<title>Test</title>

# add imports to view.py

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User

# TO-DO: add an import for forms

def index(request):
    return render(request,'home.html',{'NEXT_URL':'/demographic'})

def demographic(request):
    return render(request,'demographic.html',{'NEXT_URL':'/'})






