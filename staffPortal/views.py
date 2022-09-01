from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from studentPortal.models import Student




@login_required(login_url='login')
def dashboard(request):
    if request.user.is_staff and not request.user.is_superuser:
        return render(request, 'staffPortal/dashboard.html')

        

@login_required(login_url='login')
def student_result(request):
    if request.user.is_staff and not request.user.is_superuser:
        if request.method == "POST" and "upload" in request.POST:
            return render(request, 'staffPortal/result_upload.html')
            
        if request.method == "POST" and "update" in request.POST:
            return render(request, 'staffPortal/result_update.html')
        return render(request, 'staffPortal/student_result.html')

@login_required(login_url='login')
def assignment(request):
    if request.user.is_staff and not request.user.is_superuser:
        return render(request, 'staffPortal/assignment.html')


@login_required(login_url='login')
def materials(request):
    if request.user.is_staff and not request.user.is_superuser:
        return render(request, 'staffPortal/materials.html')

@login_required(login_url='login')
def manage_students(request):
    if request.user.is_staff and not request.user.is_superuser:
        return render(request, 'staffPortal/manage_students.html')
        
@login_required(login_url='login')
def add_student(request):
    if request.user.is_staff and not request.user.is_superuser:
        if request.method == 'POST':
            reg_no = request.POST.get('reg_no')
            state = request.POST.get('state').lower()
            password = make_password(state)
            
            try:
                User.objects.get(username=reg_no)
                
            except:
                User.objects.create(username=reg_no, password=password)
            reg_no = User.objects.get(username=reg_no)
            name = request.POST.get('name')
            programme = request.POST.get('programme')
            level = request.POST.get('level')
            lga = request.POST.get('lga')
            phone_no = request.POST.get('phone_no')
            address = request.POST.get('address')
            dob = request.POST.get('dob')
            nok = request.POST.get('nok')
            nok_phone_no = request.POST.get('nok_phone_no')
            nok_email = request.POST.get('nok_email')
            passport = request.FILES.get('passport')



            Student.objects.create(
                user = reg_no,
                name = name,
                programme = programme,
                current_level = level,
                state = state,
                lga = lga,
                phone_number = phone_no,
                home_address = address,
                dob = dob,
                next_of_kin = nok,
                next_of_kin_phone_number = nok_phone_no,
                next_of_kin_email = nok_email,
                passport = passport,
            )

        return render(request, 'staffPortal/add_student.html')
        

