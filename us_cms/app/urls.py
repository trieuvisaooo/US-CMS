from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('activity', views.activity, name='activity'),
    path('activity/<activity_id>', views.activity_detail, name='activity_detail'),
    path('login', views.login, name='login'),
]
