from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, Contact
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
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            staffProfile = UserProfile.objects.get(user=user)
            usertype = staffProfile.user_type
            if usertype == 'admin':
                return redirect('admin_page')
            elif usertype == 'app_user':
                return redirect('staff_page')
        else:
            messages.info(request, 'Username or Password is in correct')
    context = {}
    return render(request, 'login.html', context)


def admin_signup(request):
    form1 = RegisterForm()
    if request.method == 'POST':
        form1 = RegisterForm(request.POST)
        username = request.POST.get('email')
        if form1.is_valid():
            new_user = form1.save(commit=False)
            new_user.username = username
            new_user.save()
            UserProfile.objects.create(
                user=new_user,
                user_type='admin',
            )
            return redirect('admin_login')
    context = {'form1': form1}
    return render(request, 'signup.html', context)


def logout_user(request):
    logout(request)
    return redirect('admin_login')


@login_required(login_url='admin_login')
def admin_page(request):
    all_contact = Contact.objects.all()
    total_contact = all_contact.count()
    context = {'total_contact': total_contact}
    return render(request, "admin_home.html", context)


@login_required(login_url='admin_login')
def bulk_contact_upload(request):
    if request.method == "POST":
        question_link = request.POST.get("question_link")
        input = request.POST.get("confirm")
        if input == "confirm":
            url = question_link
            response = urlopen(url)
            data_json = json.loads(response.read())
            for data in data_json:
                Contact.objects.create(
                    organization=data["organization"],
                    name=data["name"],
                    phone=data["phone"],
                )
            return redirect("admin_page")
        else:
            messages.info(request, "You Entered Wrong Input")
    context = {}
    return render(request, "admin_home.html", context)


@login_required(login_url='admin_login')
def contacts_page(request):
    if request.method == "POST":
        organization = request.POST.get("organization")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        Contact.objects.create(
            organization=organization,
            name=name,
            phone=phone,
        )
    all_contact = Contact.objects.all()
    context = {'all_contact': all_contact}
    return render(request, "all_contacts.html", context)


@api_view(['POST'])
def filter_contact(request):
    if request.method == 'POST':
        data = request.data
        print("data", data['body'])
        recieved_text = data['body']
        filtered_list = Contact.objects.filter(
            Q(organization__contains=recieved_text) | Q(name__contains=recieved_text) | Q(phone__contains=recieved_text))
        serializer = ContactSerializer(filtered_list, many=True)
        return Response(serializer.data)


def filter_contact_web_page(request):
    if request.method == 'POST':
        recieved_text = request.POST.get('search_text')
        filtered_list = Contact.objects.filter(
            Q(organization__contains=recieved_text) | Q(name__contains=recieved_text) | Q(phone__contains=recieved_text))
        context = {'filtered_list': filtered_list}
        return render(request, 'home.html', context)
    context = {}
    return render(request, 'home.html', context)
