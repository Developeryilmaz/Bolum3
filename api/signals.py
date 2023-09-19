from django.contrib.auth.models import User
from api.models import Profile, StatusMessage
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # print(instance.username, '__Created: ', created)
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_first_status_message(sender, instance, created, **kwargs):
    if created:
        StatusMessage.objects.create(
            profile=instance,
            message=f'{instance.user.username} joined the club.'
        )
