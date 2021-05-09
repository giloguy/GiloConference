from django.urls import path
from app import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('contact_us/', views.contact_us, name='contact'),
]