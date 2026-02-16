from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Department, Doctor, Patient, Appointment, Prescription
from .serializers import (
    DepartmentSerializer, DoctorSerializer, PatientSerializer, AppointmentSerializer, PrescriptionSerializer,
    PrescriptionListSerializer, AppointmentListSerializer, DoctorListSerializer
)

class DepartmentListView(APIView):
    
    def get(self, request):
        try:
            department_qs = Department.objects.filter(is_active=True, is_deleted=False)
            serializer = DepartmentSerializer(department_qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        
        try:
            serializer = DepartmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e: 
            return Response({"error": str(e)}, status=500)
    
class DepartmentDetailView(APIView):
    
    def get(self, request, pk):
        try:
            queryset = Department.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DepartmentSerializer(queryset)
                return Response(serializer.data) 
            return Response({"error": "Department not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def put(self, request, pk):
        try:
            queryset = Department.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Department not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, pk):
        try:
            queryset = Department.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DepartmentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Department not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class DoctorListView(APIView):
    
    def get(self, request):
        try:
            doctor_qs = Doctor.objects.filter(is_active=True, is_deleted=False)
            serializer = DoctorListSerializer(doctor_qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        
        try:
            serializer = DoctorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e: 
            return Response({"error": str(e)}, status=500)
        
class DoctorDetailView(APIView):

    def get(self, request, pk):
        try:
            queryset = Doctor.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DoctorListSerializer(queryset)
                return Response(serializer.data) 
            return Response({"error": "Doctor not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def put(self, request, pk):
        try:
            queryset = Doctor.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DoctorSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Doctor not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, pk):
        try:
            queryset = Doctor.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = DoctorSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Doctor not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class PatientListView(APIView):

    def get(self, request):
        try:
            patient_qs = Patient.objects.filter(is_active=True, is_deleted=False)
            serializer = PatientSerializer(patient_qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        
        try:
            serializer = PatientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e: 
            return Response({"error": str(e)}, status=500)
        
class PatientDetailView(APIView):

    def get(self, request, pk):
        try:
            queryset = Patient.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PatientSerializer(queryset)
                return Response(serializer.data) 
            return Response({"error": "Patient not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def put(self, request, pk):
        try:
            queryset = Patient.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PatientSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Patient not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, pk):
        try:
            queryset = Patient.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PatientSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Patient not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class AppointmentListView(APIView):

    def get(self, request):
        try:
            appointment_qs = Appointment.objects.filter(is_active=True, is_deleted=False)
            serializer = AppointmentListSerializer(appointment_qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        
        try:
            serializer = AppointmentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e: 
            return Response({"error": str(e)}, status=500)
        
class AppointmentDetailView(APIView):

    def get(self, request, pk):
        try:
            queryset = Appointment.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = AppointmentListSerializer(queryset)
                return Response(serializer.data) 
            return Response({"error": "Appointment not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def put(self, request, pk):
        try:
            queryset = Appointment.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = AppointmentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Appointment not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, pk):
        try:
            queryset = Appointment.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = AppointmentSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Appointment not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
class PrescriptionListView(APIView):

    def get(self, request):
        try:
            prescription_qs = Prescription.objects.filter(is_active=True, is_deleted=False)
            serializer = PrescriptionListSerializer(prescription_qs, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
    
    def post(self, request):
        
        try:
            serializer = PrescriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)
            return Response(serializer.errors, status=400)
        except Exception as e: 
            return Response({"error": str(e)}, status=500)
        
class PrescriptionDetailView(APIView):

    def get(self, request, pk):
        try:
            queryset = Prescription.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PrescriptionListSerializer(queryset)
                return Response(serializer.data) 
            return Response({"error": "Prescription not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def put(self, request, pk):
        try:
            queryset = Prescription.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PrescriptionSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Prescription not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, pk):
        try:
            queryset = Prescription.objects.filter(pk=pk, is_active=True, is_deleted=False).first()
            if queryset:
                serializer = PrescriptionSerializer(queryset, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            return Response({"error": "Prescription not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)