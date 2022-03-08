import http
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def jop_list(request):
    return HttpRequest("joplist")


def jop_details(request):
    return HttpRequest("jop details")