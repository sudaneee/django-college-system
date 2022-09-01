from django.shortcuts import render
from .serializers import ApplicationFormSerializer
from form_app.models import ApplicationForm
from rest_framework import serializers, generics, permissions

class ApplicationCreate(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
    permission_classes = [permissions.IsAuthenticated]



