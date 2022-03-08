from django.db import models

# Create your models here.
# CREATE TABLE 
class Job(models.Model):
    #COLUMN TITLE
    title = models.CharField(max_length=100) 
