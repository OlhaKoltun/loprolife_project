from django.shortcuts import render


def main(request):
    return render(request, 'patients/main.html')


def patient_info(request):
    return render(request, 'patients/patient_info.html')
