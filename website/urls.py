from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('about', views.about, name='about'),
    path('course/<pk>', views.course, name='course'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<pk>', views.single_gallery, name='single-gallery'),
    path('news', views.news, name="news"),
    path('news/<pk>', views.news_single, name='news-single'),
    path('contact', views.contact, name="contact"),
]
