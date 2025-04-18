# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('brand', 'Brand'),
        ('influencer', 'Influencer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES ,default='influencer')
    
    # Common fields
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)

    # Influencer-specific
    social_links = models.JSONField(blank=True, null=True)  # {"instagram": "...", "youtube": "..."}
    followers_count = models.PositiveIntegerField(blank=True, null=True)

    # Brand-specific
    company_name = models.CharField(max_length=255, blank=True)
    brand_name = models.CharField(max_length=255, blank=True,null=True)
    website = models.URLField(blank=True)
    phone = models.CharField(max_length=20, blank=True,null=True)
    industry = models.CharField(max_length=70, blank=True,null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Campaign(models.Model):
    brand = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='campaigns')
    title = models.CharField(max_length=255)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    product_url = models.URLField(blank=True)
    target_platform = models.CharField(max_length=100)  # e.g., Instagram, TikTok
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CampaignApplication(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='applications')
    influencer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],
        default='pending'
    )
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.influencer.username} - {self.campaign.title}"


# payments/models.py


class VirtualCardRequest(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE, related_name='card_requests')
    influencer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='card_requests')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    card_issued = models.BooleanField(default=False)
    issued_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.influencer.username} - ${self.amount} for {self.campaign.title}"




class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} @ {self.timestamp}"
    




