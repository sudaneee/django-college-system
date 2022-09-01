from django.db import models

class ApplicationForm(models.Model):
    paymentReference = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phoneNo = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    lga = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.TextField()
    dob = models.CharField(max_length=200)
    nokName = models.CharField(max_length=200)
    nokPhone = models.CharField(max_length=200)
    attendedSchool1 = models.CharField(max_length=500, null=True)
    attendedSchool2 = models.CharField(max_length=500, null=True)
    attendedSchool3 = models.CharField(max_length=500, null=True)
    courseApplied = models.CharField(max_length=500)
    admitted = models.BooleanField(default=False)

    def __str__(self):
        return self.email   