from django.urls import path
from . import views


urlpatterns = [
    path('api-createApplication', views.ApplicationCreate.as_view()),
]