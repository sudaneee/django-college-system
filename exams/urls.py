from django.urls import path
from . import views


urlpatterns = [
    path('', views.exams_dashboard, name='exams-dashboard'),
    path('upload-result/', views.upload_result, name='upload-result'),
    path('update-result/', views.update_result, name='update-result'),

]