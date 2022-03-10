from unicodedata import name
from django.urls import path
from .views import jop_list , jop_details

# IT MUST TO KNOWING THIS APP TO NAVIGATE
app_name = 'job'
# IT MUST TO KNOWING THIS APP TO NAVIGATE
urlpatterns = [
    path('', jop_list, name="jobs"),
    path('jobs/<int:id>', jop_details, name='jobDetails' ),
]