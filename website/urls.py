from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login', views.loginPage, name='login'),
    # path('logout', views.logoutUser, name='logout'),
    path('about', views.about, name='about'),
    path('department/<str:department_name>', views.department, name='department'),
    path('school/<str:school_name>', views.school, name='school'),
    path('unit/<str:unit_name>', views.unit, name='unit'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<pk>', views.single_gallery, name='single-gallery'),
    path('staff-single/<pk>', views.staff_single, name='staff-single'),
    path('news', views.news, name="news"),
    path('news/<pk>', views.news_single, name='news-single'),
    path('contact', views.contact, name="website-contact"),
]
