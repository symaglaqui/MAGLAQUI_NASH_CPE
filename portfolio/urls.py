from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='about'),
    path('', views.home, name='services'),
    path('', views.home, name='portfolio'),
    path('contact.html', views.contact, name='contact'),
]