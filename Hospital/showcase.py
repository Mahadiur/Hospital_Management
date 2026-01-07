from django.shortcuts import render
from HospitalDoctor.models import hospital_doctor
from Hospitalemployee.models import HospitalEmployee
from HospitalNurse.models import hospitalnurse

def hospital_home(request):
    hos_docter = hospital_doctor.objects.all()
    hos_employee = HospitalEmployee.objects.all()
    hos_nurse = hospitalnurse.objects.all()

    hos_management_data = {
        'hospital_doctor_info' : hos_docter,
        'hospital_empolyee_info': hos_employee,
        'hospital_nurse_info': hos_nurse
    }
    
    return render(request, 'home.html', hos_management_data)