from django.contrib import admin
from meds.models import *

admin.site.register(patient)
admin.site.register(patientId)
admin.site.register(doctor)
admin.site.register(doctorId)


class AdminPatientDocument(admin.ModelAdmin):
    list_display = ['pat_id','docs_name','docs_desc','docs_image']

admin.site.register(patientDocument,AdminPatientDocument)

class AppointmentAdmin(admin.ModelAdmin):
    list_display=['patient_id','doctor_id']

admin.site.register(Appointment,AppointmentAdmin)

class ConfirmAppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_id','doctor_id','contact_date','contact_time']

admin.site.register(ConfirmAppointment,ConfirmAppointmentAdmin)

admin.site.register(PaymentDetails)

# Register your models here.


# Register your models here.