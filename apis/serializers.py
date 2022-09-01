from dataclasses import field
from rest_framework import serializers
from form_app.models import ApplicationForm

class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationForm
        fields = (
            'paymentReference',
            'email',
            'phoneNo',
            'name',
            'lga',
            'city',
            'address',
            'dob',
            'nokName',
            'nokPhone',
            'attendedSchool1',
            'attendedSchool2',
            'attendedSchool3',
            'courseApplied',
        )