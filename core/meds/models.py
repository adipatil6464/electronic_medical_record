from django.db import models



class patientId(models.Model):
    patientid = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.patientid


class patient(models.Model):
    patient_id = models.OneToOneField(patientId, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    patient_mail = models.EmailField(unique=True)
    patient_age = models.IntegerField()
    patient_address = models.CharField(max_length=100)
    patient_password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.patient_name
    
    class META:
        ordering = ['patient_name']
        verbose_name = 'patient'



# class patient(models.Model):
#     patientid = models.CharField(max_length=100)
#     patient_name = models.CharField(max_length=100)
#     patient_mail = models.EmailField(unique=True)
#     patient_age = models.IntegerField()
#     patient_address = models.CharField(max_length=100)
#     patient_password = models.CharField(max_length=100)
#     def __str__(self) -> str:
#         return self.patient_name
    
#     class META:
#         ordering = ['patient_name']
#         verbose_name = 'patient'


class patientDocument(models.Model):
    # patient = models.ForeignKey(patient, related_name='patient', on_delete=models.CASCADE)
    pat_id = models.CharField(max_length=100)
    docs_name = models.CharField(max_length=100)
    docs_desc = models.TextField()
    docs_image = models.ImageField(upload_to='docs')


    def __str__(self) -> str:
        return self.pat_id
    


class doctorId(models.Model):
    doctorid = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.doctorid



class doctor(models.Model):
    doctor_id = models.OneToOneField(doctorId, on_delete=models.CASCADE)
    doctor_name = models.CharField(max_length=100)
    doctor_mail = models.EmailField(unique=True)
    doctor_age = models.IntegerField()
    doctor_specialization = models.CharField(max_length=100)
    doctor_address = models.CharField(max_length=100)
    doctor_password = models.CharField(max_length=100)

    
    def __str__(self) -> str:
        return self.doctor_name
    
    class META:
        ordering = ['doctor_name']
        verbose_name = 'doctor'




class Appointment(models.Model):
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)


class ConfirmAppointment(models.Model):
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    contact_date = models.DateField(blank=True, null=True)
    contact_time = models.TimeField(blank=True, null=True)

class PaymentDetails(models.Model):
    patient_id = models.CharField(max_length=100)
    doctor_id = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid =models.BooleanField(default=False)

# Create your models here.


