from django.db import models

# Create your models here.
class HospitalEmployee(models.Model):
    Employee_name = models.CharField(max_length=50)
    Employee_designation = models.CharField(max_length=50)
    Employee_email = models.CharField(max_length=50, unique=True)
    Employee_phone_number = models.CharField(max_length=11, help_text='Enter Bangladesi mobile number:')
    Employee_salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'name:' + self.Employee_name + " " + 'Designation:' + self.Employee_designation