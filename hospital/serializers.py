from rest_framework.serializers import Serializer, ModelSerializer

from .models import Department, Doctor, Patient, Appointment, Prescription

class DepartmentSerializer(ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

class DoctorSerializer(ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentSerializer(ModelSerializer):

    class Meta:
        model = Appointment
        fields = "__all__"

class PrescriptionSerializer(ModelSerializer):

    class Meta:
        model = Prescription
        fields = "__all__"