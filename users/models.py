from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class userprofile(models.Model):
#     user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='userprofile',primary_key=True)
#     profile=models.ImageField(upload_to='profile_images',blank=True)
#     bio=models.TextField(blank=True)

#     def __str__(self):
#         return f"{self.user.username}"


class CustomeUser(AbstractUser):
    profile=models.ImageField(upload_to='profile_images',blank=True) #profile image is meaning full. 
    bio=models.TextField(blank=True)

    def __str__(self):
        return self.username
