# Create your views here.
#<title>Test</title>

# add imports to view.py

from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User

# TO-DO: add an import for forms

def index(request):
    return render_to_response('home.html')






