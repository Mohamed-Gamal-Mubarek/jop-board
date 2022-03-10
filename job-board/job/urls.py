from unicodedata import name
from django.urls import path
from .views import jop_list , jop_details
urlpatterns = [
    path('', jop_list, name="jobs"),
    path('jobs/<int:id>', jop_details, name='jobDetails' ),
]