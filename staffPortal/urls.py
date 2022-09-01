from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='staff-dashboard'),
    path('students-result', views.student_result, name='students-result'),
    path('assignments', views.assignment, name='assignments'),
    path('materials', views.materials, name='materials'),
    path('manage-students', views.manage_students, name='manage-students'),
    path('add-student', views.add_student, name='add-student'),

]