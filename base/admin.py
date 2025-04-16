from django.contrib import admin
from .models import *

# Register your models here.
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'bio', 'profile_picture', 'location')}),
        ('Role Info', {'fields': ('role', 'company_name', 'website', 'social_links', 'followers_count')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)


# campaigns/admin.py
from django.contrib import admin
from .models import Campaign, CampaignApplication

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'budget', 'target_platform', 'created_at')
    search_fields = ('title', 'brand__username')
    list_filter = ('target_platform',)

@admin.register(CampaignApplication)
class CampaignApplicationAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'influencer', 'status', 'applied_at')
    list_filter = ('status',)
    search_fields = ('campaign__title', 'influencer__username')


# payments/admin.py
from django.contrib import admin
from .models import VirtualCardRequest

@admin.register(VirtualCardRequest)
class VirtualCardRequestAdmin(admin.ModelAdmin):
    list_display = ('campaign', 'influencer', 'amount', 'is_approved', 'card_issued', 'created_at')
    list_filter = ('is_approved', 'card_issued')
    search_fields = ('influencer__username', 'campaign__title')


# chat/admin.py
from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'is_read', 'timestamp')
    search_fields = ('sender__username', 'receiver__username')
    list_filter = ('is_read',)
