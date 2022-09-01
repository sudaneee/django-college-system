from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return render(request, 'studentPortal/dashboard.html')
        
@login_required(login_url='login')
def school_fees(request):
    if not request.user.is_staff and not request.user.is_superuser:
        if request.method == "POST" and "history" in request.POST:
            return render(request, 'studentPortal/school_fees_reciept.html')
        
        if request.method == "POST" and "pay" in request.POST:
            pass
        return render(request, 'studentPortal/school_fees.html')

@login_required(login_url='login')
def exam(request):
    if not request.user.is_staff and not request.user.is_superuser:
        if request.method == "POST" and "result" in request.POST:
            return render(request, 'studentPortal/student_result.html')
        return render(request, 'studentPortal/exam.html')

@login_required(login_url='login')
def assignment(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return render(request, 'studentPortal/assignment.html')

@login_required(login_url='login')
def student_profile(request):
    if not request.user.is_staff and not request.user.is_superuser:
        return render(request, 'studentPortal/student_profile.html')

