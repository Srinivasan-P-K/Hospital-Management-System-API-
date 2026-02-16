from rest_framework import serializers

from .models import Department, Doctor, Patient, Appointment, Prescription

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"

class DoctorListSerializer(serializers.ModelSerializer):

    department_name = serializers.CharField(source="department.name", read_only=True)

    class Meta:
        model = Doctor
        fields = "__all__"

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = "__all__"

class AppointmentSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(source="doctor.name", read_only=True)
    patient_name = serializers.CharField(source="patient.name", read_only=True)
    class Meta:
        model = Appointment
        fields = "__all__"

class AppointmentListSerializer(serializers.ModelSerializer):

    doctor_name = serializers.CharField(source="doctor.name", read_only=True)
    patient_name = serializers.CharField(source="patient.name", read_only=True)
    class Meta:
        model = Appointment
        fields = "__all__"

class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = "__all__"

class PrescriptionListSerializer(serializers.ModelSerializer):

    appointment_date = serializers.CharField(source="appointment.appointment_date", read_only=True)
    appointment_status = serializers.CharField(source="appointment.status", read_only=True)

    class Meta:
        model = Prescription
        fields = "__all__"