from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/influencer/', views.influencer_signup, name='influencer_signup'),
    path('signup/brand/', views.brand_signup, name='brand_signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
