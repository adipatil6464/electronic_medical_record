from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from mysqlx import Auth
from meds.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse

def register(request):

    if request.method == 'POST':
        name = request.POST['name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']

        user = patient.objects.filter(patient_id__patientid = user_name)

        if user.exists():
            messages.error(request,'user already exist')
            return redirect('/register/')
        
        
        
        patientId_obj=patientId.objects.create(patientid=user_name) 
        en = patient(patient_id = patientId_obj,patient_name=name, patient_mail=email, patient_age=age, patient_address=address, patient_password=password)
        en.save()
        messages.success(request,'register successfully')

        
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        user_name=request.POST['user_name']
        password = request.POST['password']
        if patient.objects.filter(patient_id__patientid = user_name).exists():
            user = patient.objects.get(patient_id__patientid = user_name)
            if user.patient_password == password:
                return redirect(reverse('person_doc', kwargs={'pat_id':user_name}))
            else:
                messages.error(request,'wrong password')
                return redirect('/signin/')
        else:
            messages.error(request,'No Account register with this id')
            return redirect('/signin/')
        

        #or
        
    # if not patient.objects.filter(Q(patient_id__patientid = user_name) & Q(patient_password = password)).exists():
    #             messages.error(request,'patient not found or wrong credentials')
    #             return redirect('/signin/')
                
            
    # return redirect('/register/')
        
    return render(request,'login.html')






def doctor_register(request):

    if request.method == 'POST':
        name = request.POST['name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        age = request.POST['age']
        address = request.POST['address']
        password = request.POST['password']
        specialization = request.POST['specialization']

        user = doctor.objects.filter(doctor_id__doctorid = user_name)

        if user.exists():
            messages.error(request,'user already exist')
            return redirect('/doctor_register/')
        
        
        
        doctorId_obj=doctorId.objects.create(doctorid=user_name) 
        en = doctor(doctor_id = doctorId_obj,doctor_name=name, doctor_mail=email, doctor_age=age, doctor_address=address, doctor_password=password, doctor_specialization=specialization)
        en.save()
        messages.success(request,'register successfully')

        
    return render(request, 'doctor_register.html')


def doctor_signin(request):
    if request.method == 'POST':
        user_name=request.POST['user_name']
        password = request.POST['password']
        if doctor.objects.filter(doctor_id__doctorid = user_name).exists():
            user = doctor.objects.get(doctor_id__doctorid = user_name)
            if user.doctor_password == password:
                return redirect('/show_patient/')
            else:
                messages.error(request,'wrong password')
                return redirect('/doctor_signin/')
        else:
            messages.error(request,'No Account register with this id')
            return redirect('/doctor_signin/')


    return render(request,'doctor_login.html')




def addDoc(request,patient_id):

    if request.method == 'POST':
        document_name = request.POST['document_name']
        document_description = request.POST['document_description']
        add_file = request.FILES.get('add_file')

        patientDocument.objects.create(pat_id=patient_id, docs_name=document_name, docs_desc=document_description, docs_image=add_file)
    return render(request, 'adddoc.html',{'patient_id':patient_id})


def showPatient(request):
    data = patient.objects.all()

    if request.method == 'POST':
        search = request.POST['search']

        data = patient.objects.filter(Q(patient_id__patientid__icontains=search)| Q(patient_name__icontains=search))
    return render(request,'showpatient.html',{'data':data})


def showDoc(request,patient_id):
    user = patientDocument.objects.filter(pat_id=patient_id)
    return render(request,'showdoc.html',{'user':user})


def deleteDoc(request,id):
    patientDocument.objects.get(id=id).delete()
    return redirect('/show_patient/')


def updateDoc(request,id):
    queryset = patientDocument.objects.get(id=id)

    if request.method == 'POST':
        document_name = request.POST['document_name']
        document_description = request.POST['document_description']
        image = request.FILES.get('image')

        queryset.docs_name=document_name
        queryset.docs_desc=document_description

        if image:
            queryset.docs_image=image

        queryset.save()
        return redirect('/show_patient/')

    return render(request,'updatedoc.html',{'data':queryset})


def personDoc(request,pat_id):
    data = patientDocument.objects.filter(pat_id=pat_id)
    return render(request,'persondoc.html',{'data':data})


def appointment(request,pat_id,dr_id):
    patient_info= patient.objects.get(patient_id__patientid__icontains=pat_id)
    doctor_info= doctor.objects.get(doctor_id__doctorid=dr_id)
    

def showDoctor(request,pat_id):
    doctor_data = doctor.objects.all()
    patient_data = patient.objects.filter(patient_id__patientid=pat_id)

    if request.method == 'POST':
        search = request.POST['search']

        data = doctor.objects.filter(Q(doctor_name__icontains=search) | Q(doctor_specialization__icontains=search))
    return render(request,'showdoctor.html',{'data':doctor_data})

# Create your views here.


# Create your views here.
