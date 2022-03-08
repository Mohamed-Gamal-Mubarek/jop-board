from django.contrib import admin

# IMPORT MODEL TO REGISTER IN ADMIN
from .models import Category,Job
# Register your models here.
admin.site.register(Job)
admin.site.register(Category)

