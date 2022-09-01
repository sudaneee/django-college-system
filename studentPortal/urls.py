from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='student-dashboard'),
    path('school-fees', views.school_fees, name='school-fees'),
    path('exam', views.exam, name='exam'),
    path('assignment', views.assignment, name='assignment'),
    path('student-profile', views.student_profile, name='student-profile'),

]