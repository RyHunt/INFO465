from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='info465-home'),
    path('checkbox/', views.checkbox, name='info465-test'),
    path('success/', views.success, name='info465-success'),
    path('about/', views.about, name='info465-about'),
]
