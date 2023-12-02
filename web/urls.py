from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('Profile/', views.about, name='about'),
    path('blog-details/', views.blogdetails, name='blog-details'),
    path('Updates/', views.blog, name='blog'),
    path('Contact/', views.contact, name='contact'),         
    path('Gallery/', views.gallery, name='gallery'),
    path('Business-Sector/', views.servicesdetails, name='services-details'),
    path('Awards/', views.services, name='services'),

    path('single-service', views.singleservice, name='single-service'),
    path('index-2', views.index2, name='index-2'),
    # Add other URL patterns as needed
]
