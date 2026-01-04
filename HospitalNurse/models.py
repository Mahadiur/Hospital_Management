from django.db import models

# Create your models here.
class hospitalnurse(models.Model):
    Nurse_name = models.CharField(max_length=50)
    Nurse_designation = models.CharField(max_length=50)
    Nurse_email = models.CharField(max_length=50, unique=True)
    Nurse_phone_number = models.CharField(max_length=11)
    Nurse_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'name:' + self.Nurse_name + " " + 'Designation:' + self.Nurse_designation