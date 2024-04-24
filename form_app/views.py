from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from .models import *
from website.models import Course
from django.contrib import messages
from django.urls import reverse



def dashboard(request):
    return render(request, 'form_app/dashboard.html')


def biodata(request):
    try:
        biodataObject = Biodata.objects.get(user=request.user)
    except:
        biodataObject = None
    
    if request.method == "POST":
        try:
            surname = request.POST['surname']
            firstname = request.POST['firstname']
            othername = request.POST['othername']
        except:
            pass
        marital_status = request.POST['marital_status']
        gender = request.POST['gender']
        date_of_birth = request.POST['date_of_birth']
        nationality = request.POST['nationality']
        place_of_birth = request.POST['place_of_birth']
        home_town = request.POST['home_town']
        state_of_origin = request.POST['state_of_origin']
        lga_of_origin = request.POST['lga_of_origin']

        if biodataObject != None:
            # biodataObject.surname = surname
            # biodataObject.firstname = firstname
            # biodataObject.othername = othername
            biodataObject.marital_status = marital_status
            biodataObject.gender = gender
            biodataObject.date_of_birth = date_of_birth
            biodataObject.nationality = nationality
            biodataObject.place_of_birth = place_of_birth
            biodataObject.home_town = home_town
            biodataObject.state_of_origin = state_of_origin
            biodataObject.lga_of_origin = lga_of_origin
            biodataObject.save()
            messages.success(request, 'Biodata updated successfully')    
        
        else:

            Biodata.objects.create(
                user = request.user,
                surname = surname,
                firstname = firstname,
                othername = othername,
                marital_status = marital_status,
                gender = gender,
                date_of_birth = date_of_birth,
                nationality = nationality,
                place_of_birth = place_of_birth,
                home_town = home_town,
                state_of_origin = state_of_origin,
                lga_of_origin = lga_of_origin,
            )

            messages.success(request, 'Biodata created successfully')

        return redirect('biodata')

    if biodataObject != None:
        context = {
            'biodataObject': biodataObject,
        }
        

        return render(request, 'form_app/biodata.html', context)
    else:
        return render(request, 'form_app/biodata.html')



def contact(request):
    try:
        contactObject = Contact.objects.get(user=request.user)
        nextOfKinObject = NextOfKin.objects.get(user=request.user)
    except:
        contactObject = None
        nextOfKinObject = None
    
    if request.method == "POST":
        
        fullname = request.POST['fullname']
        tel1 = request.POST['tel1']
        tel2 = request.POST['tel2']
        contact_address = request.POST['contact_address']
        permanent_address = request.POST['permanent_address']


        nok_fullname = request.POST['nok_fullname']
        relationship = request.POST['relationship']
        nok_tel = request.POST['nok_tel']
        nok_email = request.POST['nok_email']

        if contactObject != None and nextOfKinObject != None:
            
            contactObject.fullname = fullname
            contactObject.tel1 = tel1
            contactObject.tel2 = tel2
            contactObject.contact_address = contact_address
            contactObject.permanent_address = permanent_address
            nextOfKinObject.nok_fullname = nok_fullname
            nextOfKinObject.relationship = relationship
            nextOfKinObject.nok_tel = nok_tel
            nextOfKinObject.nok_email = nok_email

            contactObject.save()
            nextOfKinObject.save()

            messages.success(request, 'Contact and Next of Kin Information updated successfully')
        
        else:
            Contact.objects.create(
                user = request.user,
                fullname = fullname,
                tel1 = tel1,
                tel2 = tel2,
                contact_address = contact_address,
                permanent_address = permanent_address,
            )

            NextOfKin.objects.create(
                user = request.user,
                nok_fullname = nok_fullname,
                relationship = relationship,
                nok_tel = nok_tel,
                nok_email  = nok_email,
            )

            messages.success(request, 'Contact and Next of Kin Information created successfully')

        return redirect('contact')
    
    if contactObject != None and nextOfKinObject != None:
        context = {
            'contactObject': contactObject,
            'nextOfKinObject': nextOfKinObject,
        }
        
        return render(request, 'form_app/contact.html', context)
    
    else:
        return render(request, 'form_app/contact.html')


def olevel(request):
    if request.method == "POST":

        # Getting O-Level result
        exam_type = request.POST.getlist('exam_type')
        exam_year = request.POST.getlist('exam_year')
        center_number = request.POST.getlist('center_number')
        center_name = request.POST.getlist('center_name')
        exam_number = request.POST.getlist('exam_number')
        subjects = request.POST.getlist('subject')
        grades = request.POST.getlist('grade')

        oLevelResult = {
            "exam_type": exam_type,
            "exam_year": exam_year,
            "center_number": center_number,
            "center_name": center_name,
            "exam_number": exam_number,
            "subjects": subjects,
            "grades": grades,
        }

        OLevelResults.objects.create(
            user = request.user,
            results = json.dumps(oLevelResult)
        )
        messages.success(request, 'O level uploaded successfully')
        return redirect('olevel')
    return render(request, 'form_app/olevel.html')


def picture(request):
    try:
        pictureObject = Picture.objects.get(user=request.user)
    except:
        pictureObject = None
    
    if request.method == 'POST':
        image = request.FILES['image']

        if pictureObject != None:
            pictureObject.image = image
            pictureObject.save()
        else:
            Picture.objects.create(
                user = request.user,
                image = image,
            )
        return redirect('picture')
    
    if pictureObject != None:
        context = {
            'pictureObject': pictureObject,
        }
        
        return render(request, 'form_app/picture.html', context)
    
    return render(request, 'form_app/picture.html')


def forms(request):
    
    context = {
        'programmes': Programme.objects.all(),
    }
    return render(request, 'form_app/forms.html', context)


def forms_guidelines(request, id):
    biodata = Biodata.objects.get(user=request.user)
    contact = Contact.objects.get(user=request.user)
    next_of_kin = NextOfKin.objects.get(user=request.user)
    picture = Picture.objects.get(user=request.user)
    
    if request.method == 'POST':
        programme = Programme.objects.get(id=id)
        remitta_number = "RRR"
        courseApplied.objects.create(
            user = request.user,
            programme = programme,
            remitta_number = remitta_number
        )

        messages.success(request, 'Application Submitted succefully')
        return redirect('application-preview')

    if biodata != None and contact != None and next_of_kin != None and picture != None:
        form_status = "Okay"
    
    else:
        form_status = "NotOkay"

    requirement = EntryRequirement.objects.all()



    context = {
        'requirements': requirement,
        'form_status': form_status,
    }
    return render(request, 'form_app/forms_guidelines.html', context)



def application_preview(request):
    
    olevelResults = OLevelResults.objects.get(user=request.user)
    biodata = Biodata.objects.get(user=request.user)
    contact = Contact.objects.get(user=request.user)
    next_of_kin = NextOfKin.objects.get(user=request.user)
    # alevelResults = ALevelResults.objects.get(applicant=applicant)
    olevelResults = json.loads(olevelResults.results)
    # alevelResults = json.loads(alevelResults.results)
    olevelResults["subjects_grades1"] = zip(olevelResults['subjects'][0:8], olevelResults['grades'][0:8])
    olevelResults["subjects_grades2"] = zip(olevelResults['subjects'][9:17], olevelResults['grades'][9:17])
    admission_status = "Admitted" #if applicant.admitted == True else "No admission yet"
    # alevel = zip(alevelResults['schoolName'][1:], alevelResults['year'][1:], alevelResults['grade'][1:])
    course_applied = courseApplied.objects.get(user=request.user)

    context = {
        # 'applicant': applicant,
        'olevel': olevelResults,
        # 'alevel': alevel,
        'admision_status': admission_status,
        'biodata': biodata,
        'contact': contact,
        'next_of_kin': next_of_kin,
        'course_applied': course_applied,
    }
    
    return render(request, 'form_app/form_preview.html', context)
        


# def alevel(request):
#     return render(request, 'form_app/alevel.html')














# def form_home(request):

#     if request.method == 'POST' and "form" in request.POST:
#         email = request.POST['email']
#         # Checking if email exist
#         query = Applicant.objects.filter(email=email).exists()

#         if query == False:

#             call_back_url = reverse('form-home')
#             header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
#             url = 'https://api.paystack.co/transaction/initialize'
#             data = {
#                 'email': email,
#                 'amount': 4500*100,
#                 'currency': 'NGN',
#                 'callback_url': call_back_url
#             }

#             resp = requests.post(url=url, headers=header, json=data)

            



#             redirect_url = resp.json()['data']['authorization_url']

#             return redirect(redirect_url)
#         else:
#             messages.error(request, 'Email already Exists, please use another email')
#             return render(request, 'form_app/index.html')
            


#     return render(request, 'form_app/index.html')


# def application_form(request):

#     # Redirect from payment
    
#     if request.GET.get('reference'):
#         ref = request.GET.get('reference')
#         header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
#         url = f"https://api.paystack.co/transaction/verify/{ref}"
#         resp = requests.get(url=url, headers=header)
#         resp_status = resp.json()['data']['status']
#         resp_ref = resp.json()['data']['reference']
#         context = {
#             'ref': ref
#         }
#         if resp_status == 'success' and resp_ref == ref:
#             return render(request, 'form_app/multi/index.html', context)

#     # Continue Application
    
#     if request.method == 'POST' and "form" in request.POST:
#         ref = request.POST['reference']
#         #checking if application exist
#         query = Applicant.objects.filter(paymentReference=ref).exists()

#         if not query:
#             try:

#                 header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
#                 url = f"https://api.paystack.co/transaction/verify/{ref}"
#                 resp = requests.get(url=url, headers=header)
#                 resp_status = resp.json()['data']['status']
#                 resp_ref = resp.json()['data']['reference']
#                 context ={
#                     "ref": ref
#                 }
#                 if resp_status == 'success' and resp_ref == ref:
#                     return redirect('application-form2', ref)
#             except:
#                 messages.error(request, 'Invalid or Incorrect Reference Number!')
#                 return render(request, 'form_app/application_form.html')

#         else: 
#             messages.error(request, 'Application with reference number has been submitted!')
#             return render(request, 'form_app/application_form.html')
    
#     return render(request, 'form_app/application_form.html')
    
 
#     # Submitting form
# def application_form2(request, ref):
#     if request.method == 'POST':

#         # Getting Bio data
#         email = request.POST['email']
#         tel = request.POST['tel']
#         name = request.POST['name
#         lga = request.POST['lga']
#         city = request.POST['city']
#         address = request.POST['address']
#         dob = request.POST['dob']
#         nok = request.POST['nok']
#         nokTel = request.POST['nokTel']
#         course = request.POST['course']

#         applicant = Applicant.objects.create(
#             paymentReference = ref,
#             email = email,
#             phoneNo = tel,
#             name = name,
#             lga = lga,
#             city = city,
#             address = address,
#             dob = dob,
#             nokName = nok,
#             nokPhone = nokTel,
#             courseApplied = course,
#         )

#         # Getting O-Level result
#         exam_type = request.POST.getlist('exam_type')
#         exam_year = request.POST.getlist('exam_year')
#         center_number = request.POST.getlist('center_number')
#         center_name = request.POST.getlist('center_name')
#         exam_number = request.POST.getlist('exam_number')
#         subjects = request.POST.getlist('subject')
#         grades = request.POST.getlist('grade')

#         oLevelResult = {
#             "exam_type": exam_type,
#             "exam_year": exam_year,
#             "center_number": center_number,
#             "center_name": center_name,
#             "exam_number": exam_number,
#             "subjects": subjects,
#             "grades": grades,
#         }

#         OLevelResults.objects.create(
#             applicant = applicant,
#             results = json.dumps(oLevelResult)
#         )

#         # Getting A-Level Result
#         schoolName = request.POST.getlist('schoolName')
#         year = request.POST.getlist('year')
#         grade = request.POST.getlist('grade2')

#         aLevelResult = {
#             "schoolName": schoolName,
#             "year": year,
#             "grade": grade,
#         }

#         ALevelResults.objects.create(
#             applicant = applicant,
#             results = json.dumps(aLevelResult)
#         )

#         return redirect('application-preview', ref)
    
#     context = {
#         'courses': Course.objects.all(),
#     }
#     return render(request, 'form_app/multi/index.html', context)




