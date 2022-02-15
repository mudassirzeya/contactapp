from django.urls import path
from .views import login_page, admin_signup, admin_page, contacts_page, logout_user, bulk_contact_upload, filter_contact, filter_contact_web_page

urlpatterns = [
    path('admin_login/', login_page, name='admin_login'),
    path('admin_signup/', admin_signup, name='admin_signup'),
    path('logout/', logout_user, name='logout'),
    path('', filter_contact_web_page, name='home'),
    path('admin_page/', admin_page, name='admin_page'),
    path('bulk_upload/', bulk_contact_upload, name='bulk_upload'),
    path('contact_page/', contacts_page, name='contact_page'),
    path('search_page/', filter_contact, name='search_page'),
]
