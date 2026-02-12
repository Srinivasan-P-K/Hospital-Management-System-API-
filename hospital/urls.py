from django.urls import path
from .views import (
    DepartmentListView, DepartmentDetailView, DoctorListView, DoctorDetailView,
    PatientListView, PatientDetailView, AppointmentListView, AppointmentDetailView,
    PrescriptionListView, PrescriptionDetailView
)

urlpatterns = [
    # Define your URL patterns here
    path('departments/', DepartmentListView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('patients/', PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('appointments/', AppointmentListView.as_view(), name='appointment-list'),
    path('appointments/<uuid:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),
    path('prescriptions/', PrescriptionListView.as_view(), name='prescription-list'),
    path('prescriptions/<uuid:pk>/', PrescriptionDetailView.as_view(), name='prescription-detail'),
]