"""Define URL schemes for users"""
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    # Include URL authorization by default
    path('', include('django.contrib.auth.urls')),

    # Registration page
    path('register/', views.register, name='register'),

    # Logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Logout confirmation
    path('logout/confirm/', views.logout_confirm, name='logout_confirm'),

]