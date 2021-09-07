# signal
from django.db.models.signals import post_save
# sender
from django.contrib.auth.models import User
# receiver
from django.dispatch import receiver

from .models import Profile

# runs everytime a user is created
# when a user is saved a signal is sent to this receiver function
@receiver(post_save, sender=User)
# **kwargs accepts any additional keyword arguments
def create_profile(sender, instance, created, **kwargs):
    # if a user was created, create a profile for that instance
    # of the user
    if created:
        Profile.objects.create(user=instance)

# runs everytime a user is saved and updates the users profile
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
