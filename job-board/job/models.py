from django.db import models

# Create your models here.
JOB_TYPE_CHOICE = [
    ('FT', 'Full Time'),
    ('PT', 'Part Time'),
]

# # FOCUS YOU MUST CRETE IT BEFORE TO AVOID ERRORS
# # DON'T FORGET TO MIGRATE IT
# # DON'T FORGET OT REGISTER IT ON AMDMIN


class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)
# REALTIONS


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
    #RELATION ONE TO MANY
    category = models.ForeignKey(Category, on_delete=models.CASCADE);
    # WATING FOR CATEGORY BECAUSE IT ORM (OBJECT RELATION MAPPING)
    # constructor

    def __str__(self):
        return (self.title)
