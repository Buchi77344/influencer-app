from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import *
from django.contrib import messages
from django.utils.html import escape




def index (request):
    return render (request, 'index.html')

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



def brand_signup(request):
    return render(request, 'signup_brand.html')

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

import json

@csrf_exempt
def signup_brand(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Validate email
            email = data.get('email', '')
            email_validator = EmailValidator()

            try:
                email_validator(email)
            except ValidationError:
                return JsonResponse({'error': 'Invalid email address'}, status=400)

            # Extract other fields
            brand_name = data.get('brand_name', '')
            company_name = data.get('company_name', '')
            phone = data.get('phone', '')
            website = data.get('website', '')
            industry = data.get('industry', '')
            password = data.get('password', '')
            confirm_password = data.get('confirm_password', '')

            # Password validation
            if password != confirm_password:
                return JsonResponse({'error': 'Passwords do not match'}, status=400)

            # Create user
             # This ensures you're using the CustomUser model
            user = CustomUser.objects.create_user(
                email=email,
                username=email,
                password=password,
                brand_name=brand_name,
                company_name=company_name,
                phone=phone,
                website=website,
                industry=industry,
                role= "brand"
            )

            # Return a success response
            return JsonResponse({'message': 'Signup successful!'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)



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


def option(request):
    return render (request, 'option.html')


def brand_dash(request):
    return render (request, 'brand-dash.html')