from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, UserProfile


@receiver(post_save,sender=User)   
def post_save_create_profile_receiver(sender,created,instance,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            #Create userprofile if doesnot exist....
            UserProfile.objects.create(user=instance)
            