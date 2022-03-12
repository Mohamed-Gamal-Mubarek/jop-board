from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



''' 
Focus what We Want to do in this model or what will happen next after we created this model 
1- first thing we need to do (when user is created we want to create with him profile)
focus we will use signals


https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
don't forget to see that _!!!!_
'''

class City(models.Model):
    name = models.CharField(max_length=30)

class Profile(models.Model):
    # ITS CREATED TO ADD SOMTHING TO USER 
    # RELATION ONE TO NOE TO USER
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.ForeignKey(City, related_name='user_city', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    img = models.ImageField(upload_to ="profile/")

    def __str__(self):
        # RETURNING THE NAME OF THE USER PROFILE BY NAMING IT SELF NAMING USER
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

