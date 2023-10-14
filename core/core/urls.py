"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from meds.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('signin/',signin, name='signin'),
    path('doctor_signin/',doctor_signin,name='doctor_signin'),
    path('doctor_register/',doctor_register,name='doctor_register'),
    path('show_patient/<doctor_id>',showPatient,name='showPatient'),
    path('show_doctor/<pat_id>/',showDoctor,name='showDoctor'),
    path('add_doc/<patient_id>',addDoc,name='addDoc'),
    path('show_docs/<patient_id>',showDoc,name='showDoc'),
    path('delete_doc/<id>',deleteDoc,name='deleteDoc'),
    path('update_doc/<id>',updateDoc,name='updateDoc'),
    path('person_doc/<str:pat_id>/',personDoc,name='person_doc'),
    path('appointment/<doctor_id>/<patient_id>/',appointment,name='appointment'),
    path('doctor_appointment/<doctor_id>/',doctorAppointment,name='doctorAppointment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

