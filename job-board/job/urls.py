
from django.urls import path
from .views import jop_list , jop_details, add_job

from .api import job_list_api, job_details_api

# IT MUST TO KNOWING THIS APP TO NAVIGATE
app_name = 'job'
# IT MUST TO KNOWING THIS APP TO NAVIGATE
urlpatterns = [
    path('', jop_list, name="jobs"),
    # PUTTING ANY PAGE IN HERE BEFORE SLUG TO AVOID AN ERROR 
    path('addJob', add_job, name="addJob"),
    path('jobs/<str:slug>', jop_details, name='jobDetails' ),
    # API
    path('api/jobs', job_list_api, name='jobListApi' ),
    path('api/jobs_details/<int:id>', job_details_api, name='jobDetailApi' ),
]