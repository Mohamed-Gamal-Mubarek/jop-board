from django.urls import path
from .views import jop_list , jop_details
urlpatterns = [
    path('', jop_list ),
    path('<int:id>', jop_details ),
]