from django.shortcuts import render
from .models import Donor, BloodRequest

# Create your views here.
def donor_list(request):
    donors = Donor.objects.all()
    return render(request, 'donors/donor_list.html', {'donors' : donors})

def request_list(request):
    requests = BloodRequest.objects.all()
    return render(request,'donor/request_list.html', {'requests' : requests})

def home(request):
    return render(request, 'home.html')
