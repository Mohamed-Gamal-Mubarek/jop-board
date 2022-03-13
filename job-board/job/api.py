# VIEWS SPECIFIC API
from .models import Job
from .serializers import JobSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def job_list_api(request):
    # GET ALL JOBS FROM MODLE JOBS 
    all_jobs = Job.objects.all() # RETURN TO ME AN ARRAY OF OBJECTS => JOBS
    # STORING AND CONVERTING ALL OBJECTS TO JASON
    data = JobSerializers(all_jobs, many=True).data
    return Response({'data':data})


# DON'T FORGET TO TEST IT BY EXISTING ID IN YOUR DATABASE
@api_view(['GET'])
def job_details_api(request, id):
    job_details = Job.objects.get(id=id)
    data = JobSerializers(job_details).data
    return Response({'data':data})
