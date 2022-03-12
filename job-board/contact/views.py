from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.


def sendMessage(request):
    test = None
    info = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        email = request.POST['email']

        send_mail(
            subject= subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email])

    # THAT I WILL SEND
    context = {'info': info, 'test': test}
    return(render(request, 'contact/contact.html', context))
