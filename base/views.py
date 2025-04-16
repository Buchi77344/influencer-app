from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.contrib import messages
from django.utils.html import escape

@csrf_protect
def influencer_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bio = request.POST.get('bio')
        location = request.POST.get('location')
        social_links = request.POST.get('social_links')
        followers_count = request.POST.get('followers_count')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('influencer_signup')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='influencer',
            bio=bio,
            location=location,
            social_links=social_links,
            followers_count=followers_count
        )
        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup_influencer.html')


@csrf_protect
def brand_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        company_name = request.POST.get('company_name')
        website = request.POST.get('website')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('brand_signup')

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='brand',
            company_name=company_name,
            website=website
        )
        login(request, user)
        return redirect('dashboard')

    return render(request, 'signup_brand.html')


@csrf_protect
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('login')

    return render(request, 'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
