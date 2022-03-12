
from django.urls import path
from .views import signup , profile , profile_edit

# IT MUST TO KNOWING THIS APP TO NAVIGATE
app_name = 'accounts'
# IT MUST TO KNOWING THIS APP TO NAVIGATE
urlpatterns = [
    path('signup', signup, name="signup"),
    path('profile', profile, name="profile"),
    path('profile/edit', profile_edit, name="profile_edit"),

]
