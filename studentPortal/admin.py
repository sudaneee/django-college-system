from django.contrib import admin
from .models import (
    Student,
    Fees,
    Course,
    CourseRegistration,
    Result,
)

admin.site.register(Student)
admin.site.register(Fees)
admin.site.register(Course)
admin.site.register(CourseRegistration)
admin.site.register(Result)