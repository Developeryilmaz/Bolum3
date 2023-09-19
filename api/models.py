from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # user.profile
    bio = models.CharField(max_length=300, blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile_photos/%Y/%m/')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiller'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 250 or img.width > 250:
                output_size = (250, 250)
                img.thumbnail(output_size)
                img.save(self.photo.path)


class StatusMessage(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='status')  # profile.status
    message = models.CharField(max_length=240)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.profile)

    class Meta:
        verbose_name_plural = 'Durum Mesajları'
