from turtle import title
from .models import GeneralInformation, Carousel, Picture, Paragraph, Course, Staff, Blog
from studentPortal.models import Student
from django.contrib.auth.models import User

def data_processor(request):
    query = GeneralInformation.objects.all()[0]
    carousels = Carousel.objects.all()
    about1 = Picture.objects.get(title="about1")
    choose1 = Picture.objects.get(title="choose1")
    choose_p = Paragraph.objects.get(title="choose_p")
    courses = Course.objects.all()
    staffs = Staff.objects.all()
    blogs = Blog.objects.all()
    about_header_bg = Picture.objects.get(title="about header bg")
    try:
        student = Student.objects.get(user=User.objects.get(username=request.user))
    except:
        student = None


    return {
        'data' : query,
        'carousels': carousels, 
        'about1': about1,
        'choose1': choose1,
        'choose_p': choose_p,
        'courses': courses,
        'staffs': staffs,
        'blogs': blogs,
        'about_header_bg': about_header_bg,
        'current_path': request.path,
        'student': student,
    }