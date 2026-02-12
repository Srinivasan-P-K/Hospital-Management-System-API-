from django.core.management.base import BaseCommand
from hospital.models import *
from faker import Faker
import random
import uuid
from django.utils import timezone

fake = Faker("en_IN")

class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        departments = [
            "Cardiology", "Neurology", "Orthopedics",
            "Pediatrics", "Dermatology", "ENT",
            "General Medicine", "Gynecology"
        ]

        dep_objs = []
        for dep in departments:
            dep_objs.append(Department.objects.create(name=dep))

        doctors = []
        for _ in range(20):
            doctors.append(
                Doctor.objects.create(
                    name=f"Dr. {fake.name()}",
                    department=random.choice(dep_objs)
                )
            )

        patients = []
        for _ in range(40):
            patients.append(
                Patient.objects.create(
                    name=fake.name(),
                    age=random.randint(18, 75),
                    phone=fake.phone_number()
                )
            )

        for _ in range(60):
            appointment = Appointment.objects.create(
                appointment_id=uuid.uuid4(),
                doctor=random.choice(doctors),
                patient=random.choice(patients),
                appointment_date=timezone.now(),
                status=random.choice(["Scheduled", "Completed", "Cancelled"])
            )

            Prescription.objects.create(
                prescription_id=uuid.uuid4(),
                appointment=appointment,
                medicine_name=random.choice([
                    "Paracetamol",
                    "Atorvastatin",
                    "Amoxicillin",
                    "Ibuprofen",
                    "Metformin"
                ]),
                dosage=random.choice([
                    "500mg Twice Daily",
                    "10mg Once Daily",
                    "250mg After Food"
                ])
            )

        self.stdout.write(self.style.SUCCESS("Real-world data seeded successfully!"))
