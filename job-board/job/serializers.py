# GET DATA FROM MODEL THEN CONVERT IT TO JASON
# FIRST STEP
# IMPORT SERIALIZER
from rest_framework import serializers
from .models import Job

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Job
        fields = '__all__'