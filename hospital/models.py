import uuid
from django.db import models

class CommonInfo(models.Model):

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    # created_by = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.IntegerField(null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Department(CommonInfo):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(CommonInfo):
    name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="doctors")

    def __str__(self):
        return self.name


class Patient(CommonInfo):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)


class Appointment(CommonInfo):
    appointment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="appointments")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=20)


class Prescription(CommonInfo):
    prescription_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="prescriptions")
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)

