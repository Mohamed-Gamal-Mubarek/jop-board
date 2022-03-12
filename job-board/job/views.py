from django.core.paginator import Paginator
from .forms import ApplyForm, PostJob
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Job
# Create your views here.


def jop_list(request):

    # GET ALL JOB BY THIS
    jobList = Job.objects.all()
    # GET ALL JOB

    # PAGINATION WILL BE IN HERE
    paginator = Paginator(jobList, 3)  # SHOW 1 jOB PER PAGE .
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # STORE ALL JOB IN CONTEXT
    context = {'Jobs': page_obj}
    # STORE ALL JOB IN CONTEXT

    # RETURN  ALL JOB TO RENDER DATA => RENDER DATA * , TEMPLATE YOU WANT TO VIEW , CONTEXT => SOTORE DATA
    # DATA IS ALL JOBS HERE
    return (render(request, 'job/jobs.html', context))


def jop_details(request, slug):
    # return( HttpResponse(f"this wil be an one job details by this {id}"))
    # job = Job.objects.get(id=id) GET BY ID
    job = Job.objects.get(slug=slug)  # GET BY SLUG

    # CLIENT CLICK ON THE BUTTON IN THE PAGE DETAILS JOB
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        # CHECK FORM IS VALID

        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.job = job
            myForm.save()
    else:
        form = ApplyForm()

    context = {"Job": job, 'form': form}
    return (render(request, 'job/job_details.html', context))


@login_required
# ADD JOB
def add_job(request):
    
    if request.method == 'POST':
        form = PostJob(request.POST, request.FILES)
        # CHECK FORM IS VALID
        if form.is_valid():
            myForm = form.save(commit=False)
            # CURRENT USER
            myForm.owner = request.user
            # ./CURRENT USER
            myForm.save()
            return redirect(reverse('job:jobs'))
    else:
        form = PostJob()

    context = {'form':form}
    return render(request, 'job/add_job.html', context)
