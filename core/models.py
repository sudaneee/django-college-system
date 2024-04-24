from django.db import models

# Create your models here.

class Session(models.Model):
    session_name = models.CharField(max_length=100)

    def __str__(self):
        return self.session_name
    

class Semester(models.Model):
    semester_name = models.CharField(max_length=100)

    def __str__(self):
        return self.semester_name

class School(models.Model):
    school_name = models.CharField(max_length=100)
    welcome_note = models.TextField(null=True)
    dean_picture = models.ImageField(upload_to='general pictures', null=True, blank=True)
    dean_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.school_name

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    welcome_note = models.TextField(null=True)
    head_picture = models.ImageField(upload_to='general pictures', null=True, blank=True)
    head_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.department_name

class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    welcome_note = models.TextField(null=True, blank=True)
    head_picture = models.ImageField(upload_to='general pictures', null=True, blank=True)
    head_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.unit_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    credit_unit = models.IntegerField()

    def __str__(self):
        return self.course_name

    

class SchoolFees(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'School fees for {self.school}'

class RegistrationDeclaration(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    registraion_is_on = models.BooleanField(default=False)

    def __str__(self):
        return f'Registration Declaration {self.session} Session'


class GeneralData(models.Model):
    tag = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='general pictures')
    general_preview_header = models.ImageField(upload_to='general pictures')

    def __str__(self):
        return self.tag