from enum import auto
from turtle import title
from django.db import models

# Create your models here.
# CREATE TABLE

JOB_TYPE_CHOICE = [
    ('FT', 'Full Time'),
    ('PT', 'Part Time'),
]


class Job(models.Model):
    # COLUMN TITLE
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    #WATING FOR CATEGORY BECAUSE IT ORM (OBJECT RELATION MAPPING)
    # constructor 
    def __str__(self):
        return (self.title)