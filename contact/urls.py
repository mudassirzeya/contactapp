from django.urls import path
from .views import login_page, add_admin, admin_page, contacts_home_page, logout_user, bulk_contact_upload, filter_contact, filter_contact_web_page, add_user, user_info_page, report_contact, recieve_contact_id, edit_contact, contact_profile, delete_contact, mobile_login, mobile_report_contact

urlpatterns = [
    path('admin_login/', login_page, name='admin_login'),
    path('mobile_login/', mobile_login, name='mobile_login'),
    path('add_admin/', add_admin, name='add_admin'),
    path('logout/', logout_user, name='logout'),
    path('add_user/', add_user, name='add_user'),
    path('', filter_contact_web_page, name='home'),
    path('contact_profile/<str:pk>/', contact_profile, name='contact_profile'),
    path('admin_page/', admin_page, name='admin_page'),
    path('bulk_upload/', bulk_contact_upload, name='bulk_upload'),
    path('contact_page/', contacts_home_page, name='contact_page'),
    path('contact_id/', recieve_contact_id, name='contact_id'),
    path('edit_contact/', edit_contact, name='edit_contact'),
    path('delete_contact/', delete_contact, name='delete_contact'),
    # path('filter_contact_page/', filter_contacts_page, name='filter_contact_page'),
    path('user_info_page/', user_info_page, name='user_info_page'),
    path('contact_reports/', report_contact, name='contact_reports'),
    path('mobile_contact_reports/', mobile_report_contact,
         name='mobile_contact_reports'),
    path('search_page/', filter_contact, name='search_page'),
]
