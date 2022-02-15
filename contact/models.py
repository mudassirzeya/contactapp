from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    USERTYPE = (
        ('app_user', 'app_user'),
        ('admin', 'admin'),
    )
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    profile_pic = models.ImageField(
        default="profile1.jpg", null=True, blank=True)
    user_type = models.CharField(max_length=100, blank=True, choices=USERTYPE)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    organization = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    added_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
