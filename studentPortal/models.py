from django.db import models
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
import datetime

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    programme = models.CharField(max_length=500)
    current_level = models.CharField(max_length=200)
    state = models.CharField(max_length=200,null=True)
    lga = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    home_address = models.TextField(null=True)
    dob = models.CharField(max_length=200, null=True)
    next_of_kin = models.CharField(max_length=200,null=True)
    next_of_kin_phone_number = models.CharField(max_length=200,null=True)
    next_of_kin_email = models.CharField(max_length=200,null=True)    
    passport = models.ImageField(upload_to='passports', null=True)

    def __str__(self):
        return str(self.user)
    

class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.CharField(max_length=200)
    transaction_reference = models.CharField(max_length=200)
    paid_on = models.DateTimeField(auto_now_add=True)
    amount_paid = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='NGN',
        max_digits=11,
    )

    def __str__(self):
        return str(self.student)


class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    unit = models.IntegerField()
    level = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.code

class CourseRegistration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.CharField(max_length=200)
    semester = models.CharField(max_length=200)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.student)

class Result(models.Model):
    registered_course = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_a = models.IntegerField()
    exams = models.IntegerField()

    def total(self):
        self.c_a + self.exams

    def __str__(self):
        return str(self.registered_course)


