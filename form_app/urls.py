from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('biodata/', views.biodata, name='biodata'),
    path('contact/', views.contact, name='contact'),
    path('olevel/', views.olevel, name='olevel'),
    path('picture/', views.picture, name='picture'),
    path('forms/', views.forms, name='forms'),
    path('forms-guidelines/<int:id>/', views.forms_guidelines, name='forms-guidelines'),
    path('application-preview/', views.application_preview, name='application-preview'),
    

]