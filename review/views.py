from django.shortcuts import render, redirect
from .models import patient
# Create your views here.
from django.contrib import messages

def home(request):
        r=patient.objects.all().values()

        return render(request, 'home.html',{"r":r})





def index(request):

    if request.method == 'POST':
        Review1 = patient(
            FIRST_NAME=request.POST['firstname'],

            LAST_NAME=request.POST['lastname'],

            Gender=request.POST['gender'],

            Hospital_Name=request.POST['HospitalName'],

            Phone=request.POST['phone'],

            REVIEW=request.POST['writereview'])

        if patient.objects.filter(Phone=Review1.Phone).exists():
                messages.warning(request, 'Phone Is Already Exists')
                return redirect('/index')
        else:
                Review1.save()
                messages.success(request, 'Data Save  Successfuly')
                return redirect('/')

    else:
        return render(request, 'index.html')






