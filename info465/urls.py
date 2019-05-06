from django.urls import path
from . import views
from django.conf.urls import include
# my_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='info465/home.html'), name='info465-home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('checkbox/', views.checkbox, name='info465-test'),
    path('success/', views.success, name='info465-success'),
    path('about/', views.about, name='info465-about'),
    path('members/', views.members, name='info465-members'),

]
