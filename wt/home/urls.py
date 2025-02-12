from django.urls import path , include
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('services/it/', views.it_ser, name='it_ser'),
    path('services/material/', views.mat_ser, name='mat_ser'),
    path('services/contact_form/', views.ser_cont, name='ser_cont'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('contactUS/', views.contactus, name='contactus'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.blog_full, name='blog_full'),
    path('blog_c/', views.blog_c, name='blog_c'),
    path('WorkWithUS/', views.WorkWithUS, name='WorkWithUS'),
]
