from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

def surveys(request):
    response = "placeholder to display all surveys created"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to add a new survey"
    return HttpResponse(response)

