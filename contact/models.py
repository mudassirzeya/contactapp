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
    phone = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    user_type = models.CharField(max_length=100, blank=True, choices=USERTYPE)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    phone_label = models.CharField(max_length=200, null=True, blank=True)
    phone_is_whatsapp = models.CharField(max_length=200, null=True, blank=True)
    phone_2 = models.CharField(max_length=100, null=True, blank=True)
    phone_2_label = models.CharField(max_length=200, null=True, blank=True)
    phone_2_is_whatsapp = models.CharField(
        max_length=200, null=True, blank=True)
    phone_3 = models.CharField(max_length=100, null=True, blank=True)
    phone_3_label = models.CharField(max_length=200, null=True, blank=True)
    phone_3_is_whatsapp = models.CharField(
        max_length=200, null=True, blank=True)
    phone_4 = models.CharField(max_length=100, null=True, blank=True)
    phone_4_label = models.CharField(max_length=200, null=True, blank=True)
    phone_4_is_whatsapp = models.CharField(
        max_length=200, null=True, blank=True)
    phone_5 = models.CharField(max_length=100, null=True, blank=True)
    phone_5_label = models.CharField(max_length=200, null=True, blank=True)
    phone_5_is_whatsapp = models.CharField(
        max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    email_label = models.CharField(max_length=200, null=True, blank=True)
    email_2 = models.CharField(max_length=200, null=True, blank=True)
    email_2_label = models.CharField(max_length=200, null=True, blank=True)
    email_3 = models.CharField(max_length=200, null=True, blank=True)
    email_3_label = models.CharField(max_length=200, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    pin_code = models.CharField(max_length=200, null=True, blank=True)
    photo = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=500, null=True, blank=True)
    added_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)


class Report_Contact(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE
    )
    contact = models.ForeignKey(
        Contact, null=True, blank=True, on_delete=models.CASCADE)
    report_note = models.CharField(max_length=500, null=True, blank=True)
    added_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)
