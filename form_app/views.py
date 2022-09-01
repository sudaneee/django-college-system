from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from .models import ApplicationForm
from django.contrib import messages



def form_home(request):

    if request.method == 'POST' and "form" in request.POST:
        email = request.POST['email']
        # Checking if email exist
        query = ApplicationForm.objects.filter(email=email).exists()

        if not query:


            header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
            url = 'https://api.paystack.co/transaction/initialize'
            data = {
                'email': email,
                'amount': 500*100,
                'currency': 'NGN',
                'callback_url': 'http://127.0.0.1:8000/form/apply'
            }

            resp = requests.post(url=url, headers=header, json=data)

            



            redirect_url = resp.json()['data']['authorization_url']

            return redirect(redirect_url)
        else:
            messages.error(request, 'Email already Exists, please use another email')
            return render(request, 'form_app/index.html')
            


    return render(request, 'form_app/index.html')


def application_form(request):

    # Redirect from payment
    
    if request.GET.get('reference'):
        ref = request.GET.get('reference')
        header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
        url = f"https://api.paystack.co/transaction/verify/{ref}"
        resp = requests.get(url=url, headers=header)
        resp_status = resp.json()['data']['status']
        resp_ref = resp.json()['data']['reference']
        context = {
            'ref': ref
        }
        if resp_status == 'success' and resp_ref == ref:
            return render(request, 'form_app/multi/index.html', context)

    # Continue Application
    
    if request.method == 'POST' and "form" in request.POST:
        ref = request.POST['reference']
        #checking if application exist
        query = ApplicationForm.objects.filter(paymentReference=ref).exists()

        if not query:
            try:

                header = {'Authorization': 'Bearer sk_live_d1ef85e474c6068c3bebf0d69f44c569ece66fb9'}
                url = f"https://api.paystack.co/transaction/verify/{ref}"
                resp = requests.get(url=url, headers=header)
                resp_status = resp.json()['data']['status']
                resp_ref = resp.json()['data']['reference']
                context ={
                    "ref": ref
                }
                if resp_status == 'success' and resp_ref == ref:
                    return render(request, 'form_app/multi/index.html', context)
            except:
                messages.error(request, 'Invalid or Incorrect Reference Number!')
                return render(request, 'form_app/application_form.html')

        else: 
            messages.error(request, 'Application with reference number has been submitted!')
            return render(request, 'form_app/application_form.html')

        
        

    return render(request, 'form_app/application_form.html')