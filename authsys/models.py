from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/profile')
    facebook_url = models.URLField(max_length = 255, blank=True, null=True)
    twitter_url = models.URLField(max_length = 255, blank=True, null=True)
    instagram_url = models.URLField(max_length = 255, blank=True, null=True)

    def __str__(self):
        return str(self.user)