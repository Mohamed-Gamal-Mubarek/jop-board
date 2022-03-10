from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Job
# Create your views here.


def jop_list(request):

    # GET ALL JOB BY THIS
    jobList = Job.objects.all()
    # GET ALL JOB

    # PAGINATION WILL BE IN HERE
    paginator = Paginator(jobList, 1)  # SHOW 1 jOB PER PAGE .
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # STORE ALL JOB IN CONTEXT
    context = {'Jobs': page_obj}
    # STORE ALL JOB IN CONTEXT

    # RETURN  ALL JOB TO RENDER DATA => RENDER DATA * , TEMPLATE YOU WANT TO VIEW , CONTEXT => SOTORE DATA
    # DATA IS ALL JOBS HERE
    return (render(request, 'job/jobs.html', context))


def jop_details(request, id):
    # return( HttpResponse(f"this wil be an one job details by this {id}"))
    job = Job.objects.get(id=id)
    context = {"Job": job}
    return (render(request, 'job/job_details.html', context))
