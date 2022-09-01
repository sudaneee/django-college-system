
from .models import Course, Gallery, Blog
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout



def loginPage(request):
    
    page = 'login'
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect(reverse('admin:index'))
        elif request.user.is_staff:
            return redirect(reverse('staff-dashboard'))
        # return redirect('home')
        else:
            return redirect(reverse('student-dashboard'))


    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')


        try:
            user = User.objects.get(username=username)
            
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect(reverse('admin:index'))

            elif user.is_staff:
                return redirect(reverse('staff-dashboard'))
            # return redirect('home')
            else:
                return redirect(reverse('student-dashboard'))
            
     

        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'website/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')




def home(request):
    print('hello')
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')

def course(request, pk):
    c = Course.objects.get(id=pk)
    context = {
        'course': c,
    }
    return render(request, 'website/course.html', context)


def gallery(request):

    gallery_object = Gallery.objects.all()
    context = {
        'gallery_object': gallery_object,
    }

    return render(request, 'website/gallery.html', context)



def single_gallery(request, pk):
    c = Gallery.objects.get(id=pk)
    context = {
        'single_gallery': c,
    }
    return render(request, 'website/single-gallery.html', context)



def news(request):
    c = Blog.objects.all()
    context = {
        'news': c
    }
    return render(request, 'website/news.html', context)


def news_single(request, pk):
    c = Blog.objects.get(id=pk)
    b = Blog.objects.all()
    context = {
        'news_single': c,
        'news': b
    }
    return render(request, 'website/news-single.html', context)


def contact(request):
    return render(request, 'website/contact.html')