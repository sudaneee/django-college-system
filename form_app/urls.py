from django.urls import path
from . import views


urlpatterns = [
    path('', views.form_home, name='form-home'),
    path('application-form', views.application_form, name='application-form'),
]