from django.db import models


class Patient(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name


class PatientStatus(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    phe_analysis = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    # Add other fields related to patient status

    def __str__(self):
        return f"{self.patient.name}'s status on {self.date}"
