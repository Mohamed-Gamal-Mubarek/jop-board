from django.shortcuts import render
from .models import Info
# Create your views here.

def sendMessage(request):
    info =Info.objects.first()


    #THAT I WILL SEND
    context= {'info':info}
    return(render(request, 'contact/contact.html',context))
