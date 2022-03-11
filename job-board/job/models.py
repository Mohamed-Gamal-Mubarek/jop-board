from unicodedata import name
from django.db import models
from django.utils.text import slugify


# Create your models here.
JOB_TYPE_CHOICE = [
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
]

# # FOCUS YOU MUST CRETE IT BEFORE TO AVOID ERRORS
# # DON'T FORGET TO MIGRATE IT
# # DON'T FORGET OT REGISTER IT ON AMDMIN


class Category (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.name)


# UPLOAD IMAGE
def upload_image(instance, fileName):
    # INSTANCE REFER TO TH MODEL OBJECT
    # FILE NAME REFER TO IMAGE UPLOAD
    imageName, extention = fileName.split(".")
    # PUTTING THE NAME OF AN IMAGE NUMBER BECAUSE IT EASY ON SEARCH (PENDING)
    return (f"jobs/{instance.id}/{instance.title}/{instance.id}.{extention}")
# ./UPLOAD IMAGE


class Job(models.Model):
    # COLUMN TITLE
    title = models.CharField(max_length=100)
    # location
    type = models.CharField(max_length=100, choices=JOB_TYPE_CHOICE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
    # RELATION ONE TO MANY
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # WATING FOR CATEGORY BECAUSE IT ORM (OBJECT RELATION MAPPING)
    img = models.ImageField(upload_to=upload_image)
    slug = models.SlugField(null=True, blank=True)

    # MAKE SLUG FIELD
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
    # CONSTRUCTOR
    def __str__(self):
        return (self.title)
    # CONSTRUCTOR


class Apply(models.Model):
    job = models.ForeignKey(Job , related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name