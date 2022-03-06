from itertools import count
from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Report_Contact, UserProfile, Contact
from django.contrib import messages
from .forms import RegisterForm
from .serializers import ContactSerializer
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.db.models import Q
from urllib.request import urlopen
import json


# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("user", password, username)
        user = authenticate(request, username=username, password=password)
        print("us", user)
        if user is not None:
            login(request, user)
            staffProfile = UserProfile.objects.get(user=user)
            usertype = staffProfile.user_type
            if usertype == 'admin':
                return redirect('admin_page')
            elif usertype == 'app_user':
                return redirect('/')
        else:
            messages.info(request, 'Username or Password is in correct')
    context = {}
    return render(request, 'login.html', context)


@login_required(login_url='admin_login')
def add_admin(request):
    admin_user = UserProfile.objects.filter(user_type='admin')
    if request.method == "POST":
        username = request.POST.get("username")
        passcode = request.POST.get("passcode")
        name = request.POST.get("name")
        try:
            already_user = User.objects.get(username=username)
        except Exception:
            already_user = None
            print('user', already_user)
        if already_user is None:
            new_user = User.objects.create_user(
                username=username, password=passcode, first_name=name)
            UserProfile.objects.create(
                user=new_user,
                phone=username,
                password=passcode,
                user_type='admin',
            )
            return redirect('add_admin')
        else:
            messages.info(
                request, 'This Phone Number is already exist in our DataBase')
            return redirect('add_admin')
    context = {'admin_user': admin_user}
    return render(request, "my_team.html", context)


@login_required(login_url='admin_login')
def add_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        passcode = request.POST.get("passcode")
        name = request.POST.get("name")
        try:
            already_user = User.objects.get(username=username)
        except Exception:
            already_user = None
            print('user', already_user)
        if already_user is None:
            new_user = User.objects.create_user(
                username=username, password=passcode, first_name=name)
            UserProfile.objects.create(
                user=new_user,
                phone=username,
                password=passcode,
                user_type='app_user',
            )
            return redirect('user_info_page')
        else:
            messages.info(
                request, 'This Phone Number is already exist in our DataBase')
            return redirect('user_info_page')
    context = {}
    return render(request, "userprofile.html", context)


def logout_user(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
def admin_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    usertype = staffProfile.user_type
    if usertype == 'app_user':
        return redirect('/')
    all_contact = Contact.objects.all()
    total_contact = all_contact.count()
    userprofile = UserProfile.objects.filter(user_type='app_user')
    total_mobile_user = userprofile.count()
    context = {'total_contact': total_contact,
               'total_mobile_user': total_mobile_user}
    return render(request, "admin_home.html", context)


@login_required(login_url='admin_login')
def bulk_contact_upload(request):
    if request.method == "POST":
        # Contact.objects.all().delete()
        question_link = request.POST.get("question_link")
        input = request.POST.get("confirm")
        if input == "confirm":
            url = question_link
            response = urlopen(url)
            data_json = json.loads(response.read())
            print('data', data_json[0]['name'])
            # Contact.objects.bulk_create([data_json])

            bulk_list = list()
            for contact in data_json:
                bulk_list.append(
                    Contact(
                        name=contact['name'],
                        designation=contact['designation'],
                        department=contact['department'],
                        company=contact['company'],
                        phone=contact['phone'],
                        phone_label=contact['phone_label'],
                        phone_is_whatsapp=contact['phone_is_whatsapp'],
                        phone_2=contact['phone_2'],
                        phone_2_label=contact['phone_2_label'],
                        phone_2_is_whatsapp=contact['phone_2_is_whatsapp'],
                        phone_3=contact['phone_3'],
                        phone_3_label=contact['phone_3_label'],
                        phone_3_is_whatsapp=contact['phone_3_is_whatsapp'],
                        phone_4=contact['phone_4'],
                        phone_4_label=contact['phone_4_label'],
                        phone_4_is_whatsapp=contact['phone_4_is_whatsapp'],
                        phone_5=contact['phone_5'],
                        phone_5_label=contact['phone_5_label'],
                        phone_5_is_whatsapp=contact['phone_5_is_whatsapp'],
                        email=contact['email'],
                        email_label=contact['email_label'],
                        email_2=contact['email_2'],
                        email_2_label=contact['email_2_label'],
                        email_3=contact['email_3'],
                        email_3_label=contact['email_3_label'],
                        website=contact['website'],
                        address=contact['address'],
                        city=contact['city'],
                        state=contact['state'],
                        country=contact['country'],
                        pin_code=contact['pin_code'],
                        photo=contact['photo'],
                        notes=contact['notes'],
                    )
                )
            Contact.objects.bulk_create(bulk_list)
            # for data in data_json:
            # key_list = list(data.keys())
            # Contact.objects.bulk_create(data)
            # val_list = list(my_dict.values())

            return redirect("admin_page")
        else:
            messages.info(request, "You Entered Wrong Input")
            return redirect('admin_page')
    context = {}
    return render(request, "admin_home.html", context)


@login_required(login_url='admin_login')
def user_info_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    usertype = staffProfile.user_type
    if usertype == 'app_user':
        return redirect('/')
    all_user = UserProfile.objects.filter(user_type='app_user')
    context = {'all_user': all_user}
    return render(request, "userprofile.html", context)


@login_required(login_url='admin_login')
def contacts_home_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    usertype = staffProfile.user_type
    if usertype == 'app_user':
        return redirect('/')
    if request.method == "POST":
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        department = request.POST.get("department")
        company = request.POST.get("company")
        phone_1 = request.POST.get("phone_1")
        label_1 = request.POST.get("label_1")
        whatsapp_1 = request.POST.get("whatsapp_1")
        phone_2 = request.POST.get("phone_2")
        label_2 = request.POST.get("label_2")
        whatsapp_2 = request.POST.get("whatsapp_2")
        phone_3 = request.POST.get("phone_3")
        label_3 = request.POST.get("label_3")
        whatsapp_3 = request.POST.get("whatsapp_3")
        phone_4 = request.POST.get("phone_4")
        label_4 = request.POST.get("label_4")
        whatsapp_4 = request.POST.get("whatsapp_4")
        phone_5 = request.POST.get("phone_5")
        label_5 = request.POST.get("label_5")
        whatsapp_5 = request.POST.get("whatsapp_5")
        email = request.POST.get("email")
        email_label = request.POST.get("email_label")
        email_2 = request.POST.get("email_2")
        email_2_label = request.POST.get("email_2_label")
        email_3 = request.POST.get("email_3")
        email_3_label = request.POST.get("email_3_label")
        website = request.POST.get("website")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pincode = request.POST.get("pincode")
        photo = request.POST.get("photo")
        notes = request.POST.get("notes")

        Contact.objects.create(
            name=name,
            designation=designation,
            department=department,
            company=company,
            phone=phone_1,
            phone_label=label_1,
            phone_is_whatsapp=whatsapp_1,
            phone_2=phone_2,
            phone_2_label=label_2,
            phone_2_is_whatsapp=whatsapp_2,
            phone_3=phone_3,
            phone_3_label=label_3,
            phone_3_is_whatsapp=whatsapp_3,
            phone_4=phone_4,
            phone_4_label=label_4,
            phone_4_is_whatsapp=whatsapp_4,
            phone_5=phone_5,
            phone_5_label=label_5,
            phone_5_is_whatsapp=whatsapp_5,
            email=email,
            email_label=email_label,
            email_2=email_2,
            email_2_label=email_2_label,
            email_3=email_3,
            email_3_label=email_3_label,
            website=website,
            address=address,
            city=city,
            state=state,
            country=country,
            pin_code=pincode,
            photo=photo,
            notes=notes,
        )
        return redirect('contact_page')
    if request.method == "GET":
        contact = Contact.objects.all()
        searched_text = request.GET.get("text")
        if searched_text:
            split_text = searched_text.split()
            for text in split_text:
                contact = contact.filter(
                    Q(name__contains=text) | Q(designation__contains=text)
                    | Q(department__contains=text) | Q(company__contains=text)
                    | Q(phone__contains=text) | Q(phone_2__contains=text)
                    | Q(phone_3__contains=text) | Q(phone_4__contains=text)
                    | Q(phone_5__contains=text) | Q(email__contains=text)
                    | Q(email_2__contains=text) | Q(email_3__contains=text)
                    | Q(website__contains=text) | Q(address__contains=text)
                    | Q(city__contains=text) | Q(state__contains=text)
                    | Q(country__contains=text) | Q(pin_code__contains=text)
                )
    # all_contact = Contact.objects.all()
        pages = Paginator(contact, 100)
        page_num = request.GET.get('page', 1)
        try:
            page = pages.page(page_num)
        except EmptyPage:
            page = pages.page(1)
        context = {'all_contact': page, 'text': searched_text}
        return render(request, "all_contacts.html", context)


# @login_required(login_url='admin_login')
# def filter_contacts_page(request):
#     if request.method == "GET":
#         contact = Contact.objects.all()
#         searched_text = request.GET.get("text")
#         split_text = searched_text.split()
#         # final_list = []
#         for text in split_text:
#             contact = contact.filter(
#                 Q(name__contains=text) | Q(designation__contains=text)
#                 | Q(department__contains=text) | Q(company__contains=text)
#                 | Q(phone__contains=text) | Q(phone_2__contains=text)
#                 | Q(phone_3__contains=text) | Q(phone_4__contains=text)
#                 | Q(phone_5__contains=text) | Q(email__contains=text)
#                 | Q(email_2__contains=text) | Q(email_3__contains=text)
#                 | Q(website__contains=text) | Q(address__contains=text)
#                 | Q(city__contains=text) | Q(state__contains=text)
#                 | Q(country__contains=text) | Q(pin_code__contains=text)
#             )
#         pages = Paginator(contact, 100)
#         page_num = request.GET.get('page', 1)
#         try:
#             page = pages.page(page_num)
#         except EmptyPage:
#             page = pages.page(1)
#         context = {'all_contact': page}
#         return render(request, "all_contacts.html", context)
#     else:
#         messages.info(
#             request, 'Something Went Wrong, please try again')
#         return render(request, "all_contacts.html")
    # return render(request, "all_contacts.html", context)


@login_required(login_url='admin_login')
def report_contact(request):
    if request.method == 'POST':
        report = request.POST.get("report")
        contact_id = request.POST.get("contact_id")
        contact = Contact.objects.get(id=int(contact_id))
        Report_Contact.objects.create(
            user=request.user,
            contact=contact,
            report_note=report,
        )
        return redirect('contact_profile', pk=int(contact_id))
    all_report = Report_Contact.objects.all()
    context = {'all_report': all_report}
    return render(request, "report_contact.html", context)


@api_view(['POST'])
def filter_contact(request):
    if request.method == 'POST':
        data = request.data
        print("data", data['body'])
        recieved_text = data['body']
        split_text = recieved_text.split()
        # final_list = []
        contact = Contact.objects.all()
        for text in split_text:
            contact = contact.filter(
                Q(name__contains=text) | Q(designation__contains=text)
                | Q(department__contains=text) | Q(company__contains=text)
                | Q(phone__contains=text) | Q(phone_2__contains=text)
                | Q(phone_3__contains=text) | Q(phone_4__contains=text)
                | Q(phone_5__contains=text) | Q(email__contains=text)
                | Q(email_2__contains=text) | Q(email_3__contains=text)
                | Q(website__contains=text) | Q(address__contains=text)
                | Q(city__contains=text) | Q(state__contains=text)
                | Q(country__contains=text) | Q(pin_code__contains=text)
            )
        print("con", contact)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)


@login_required(login_url='admin_login')
def filter_contact_web_page(request):
    user = request.user
    staffProfile = UserProfile.objects.get(user=user)
    if request.method == 'GET':
        contact = Contact.objects.all()
        searched_text = request.GET.get("text")
        if searched_text:
            split_text = searched_text.split()
            for text in split_text:
                contact = contact.filter(
                    Q(name__contains=text) | Q(designation__contains=text)
                    | Q(department__contains=text) | Q(company__contains=text)
                    | Q(phone__contains=text) | Q(phone_2__contains=text)
                    | Q(phone_3__contains=text) | Q(phone_4__contains=text)
                    | Q(phone_5__contains=text) | Q(email__contains=text)
                    | Q(email_2__contains=text) | Q(email_3__contains=text)
                    | Q(website__contains=text) | Q(address__contains=text)
                    | Q(city__contains=text) | Q(state__contains=text)
                    | Q(country__contains=text) | Q(pin_code__contains=text)
                )
    # all_contact = Contact.objects.all()
        pages = Paginator(contact, 100)
        page_num = request.GET.get('page', 1)
        try:
            page = pages.page(page_num)
        except EmptyPage:
            page = pages.page(1)
        context = {'filtered_list': page,
                   'text': searched_text, "staffProfile": staffProfile}
        return render(request, 'home.html', context)
    {"staffProfile": staffProfile}
    return render(request, 'home.html', context)


def recieve_contact_id(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("data", data)
        contact_id = data["data_obj"][0]
        contact = Contact.objects.filter(
            id=int(contact_id['contact_id']))
        print('con', contact)
        contact_json = serializers.serialize('json', contact)
        print('contact', contact_json)
        return JsonResponse({"msg": "success", "data": contact_json})
    return render(request, "all_contacts.html")


def edit_contact(request):
    if request.method == "POST":
        contact_id = request.POST.get('contact_id')
        name = request.POST.get("name")
        designation = request.POST.get("designation")
        department = request.POST.get("department")
        company = request.POST.get("company")
        phone_1 = request.POST.get("phone_1")
        label_1 = request.POST.get("label_1")
        whatsapp_1 = request.POST.get("whatsapp_1")
        phone_2 = request.POST.get("phone_2")
        label_2 = request.POST.get("label_2")
        whatsapp_2 = request.POST.get("whatsapp_2")
        phone_3 = request.POST.get("phone_3")
        label_3 = request.POST.get("label_3")
        whatsapp_3 = request.POST.get("whatsapp_3")
        phone_4 = request.POST.get("phone_4")
        label_4 = request.POST.get("label_4")
        whatsapp_4 = request.POST.get("whatsapp_4")
        phone_5 = request.POST.get("phone_5")
        label_5 = request.POST.get("label_5")
        whatsapp_5 = request.POST.get("whatsapp_5")
        email = request.POST.get("email")
        email_label = request.POST.get("email_label")
        email_2 = request.POST.get("email_2")
        email_2_label = request.POST.get("email_2_label")
        email_3 = request.POST.get("email_3")
        email_3_label = request.POST.get("email_3_label")
        website = request.POST.get("website")
        address = request.POST.get("address")
        city = request.POST.get("city")
        state = request.POST.get("state")
        country = request.POST.get("country")
        pincode = request.POST.get("pincode")
        photo = request.POST.get("photo")
        notes = request.POST.get("notes")
        contact = Contact.objects.get(id=int(contact_id))

        # editing the field below
        contact.name = name
        contact.designation = designation
        contact.department = department
        contact.company = company
        contact.phone = phone_1
        contact.phone_label = label_1
        contact.phone_is_whatsapp = whatsapp_1
        contact.phone_2 = phone_2
        contact.phone_2_label = label_2
        contact.phone_2_is_whatsapp = whatsapp_2
        contact.phone_3 = phone_3
        contact.phone_3_label = label_3
        contact.phone_3_is_whatsapp = whatsapp_3
        contact.phone_4 = phone_4
        contact.phone_4_label = label_4
        contact.phone_4_is_whatsapp = whatsapp_4
        contact.phone_5 = phone_5
        contact.phone_5_label = label_5
        contact.phone_5_is_whatsapp = whatsapp_5
        contact.email = email
        contact.email_label = email_label
        contact.email_2 = email_2
        contact.email_2_label = email_2_label
        contact.email_3 = email_3
        contact.email_3_label = email_3_label
        contact.website = website
        contact.address = address
        contact.city = city
        contact.state = state
        contact.country = country
        contact.pin_code = pincode
        contact.photo = photo
        contact.notes = notes
        contact.save()
        return redirect('contact_page')
    return render(request, "all_contacts.html")


def delete_contact(request):
    if request.method == "POST":
        contact_id = request.POST.get('delete_id')
        contact = Contact.objects.get(id=int(contact_id))
        contact.delete()
        print("del", contact)
        return redirect('contact_page')
    context = {}
    return render(request, "all_contacts.html", context)


def contact_profile(request, pk):
    contact = Contact.objects.get(id=pk)
    # print("edit", contact)
    context = {"contact": contact}
    return render(request, "contact_profile.html", context)
