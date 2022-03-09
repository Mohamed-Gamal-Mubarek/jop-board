
from django.http import HttpResponse
from django.shortcuts import render

from .models import Job
# Create your views here.


def jop_list(request):
    jobList = Job.objects.all()
    context = {'jobs': jobList}
    return (render(request, 'job/job_list.html', context))

def jop_details(request, id):
    # return( HttpResponse(f"this wil be an one job details by this {id}"))
    job = Job.objects.get(id=id)
    context = {"job": job}
    return (render(request, 'job/job.html', context))