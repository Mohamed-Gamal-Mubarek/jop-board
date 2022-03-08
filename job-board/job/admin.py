from django.contrib import admin

# IMPORT MODEL TO REGISTER IN ADMIN
from .models import Job
# Register your models here.
admin.site.register(Job)

