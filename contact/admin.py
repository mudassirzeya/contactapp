from django.contrib import admin
from .models import Report_Contact, UserProfile, Contact

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(Report_Contact)
