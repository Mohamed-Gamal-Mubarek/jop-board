
from django.urls import path
from .views import sendMessage

# IT MUST TO KNOWING THIS APP TO NAVIGATE
app_name = 'contact'
# IT MUST TO KNOWING THIS APP TO NAVIGATE

urlpatterns = [
    path('/', sendMessage , name="contactPage"),
]