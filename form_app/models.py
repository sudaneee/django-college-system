from django.db import models
from django.contrib.auth.models import User

class Biodata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    othername = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    date_of_birth = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    place_of_birth = models.CharField(max_length=200)
    home_town = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=200)
    lga_of_origin = models.CharField(max_length=200)



    def __str__(self):
        return f"Bio Data for {self.user}" 

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    tel1 = models.CharField(max_length=200)
    tel2 = models.CharField(max_length=200)
    contact_address = models.TextField()
    permanent_address = models.TextField()

    def __str__(self):
       return f"Contact Info for {self.user}"

class NextOfKin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nok_fullname = models.CharField(max_length=200)
    relationship = models.CharField(max_length=200)
    nok_tel = models.CharField(max_length=200)
    nok_email = models.CharField(max_length=200)

    def __str__(self):
       return f"Next of kin for {self.user}"

class OLevelResults(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    results = models.TextField()  

    def __str__(self):
        return f"O-level Results for {self.user}"
    

class Picture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='passports')

    def __str__(self):
        return f"Picture for {self.user}"
    


class Programme(models.Model):
    programme_name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.programme_name


class courseApplied(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    remitta_number = models.CharField(max_length=200)
    programme = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f" Course Applied for {self.user}"
    


class EntryRequirement(models.Model):
    requirement = models.CharField(max_length=300)

    def __str__(self):
        return self.requirement