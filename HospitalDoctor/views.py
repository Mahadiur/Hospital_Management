from django.shortcuts import render, get_object_or_404
from .models import hospital_doctor

# Create your views here.
def doctor_details(request, pk):
    doctor = get_object_or_404(hospital_doctor, pk=pk)
    doctor_information = {
        'doctor_info': doctor,
    }
    return render(request, 'Doctor_details.html', doctor_information)