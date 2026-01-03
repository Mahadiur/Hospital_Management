from django.db import models

# Create your models here.
class hospital_doctor(models.Model):
    Doctor_name = models.CharField(max_length=50)
    Doctor_designation = models.CharField(max_length=50)
    Doctor_email = models.CharField(max_length=50, unique=True)
    Doctor_phone_number = models.CharField(max_length=11)
    Doctor_salary = models.DecimalField(max_digits=10, decimal_places=3)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'name:' + self.Doctor_name + " " + 'Designation:' + self.Doctor_designation