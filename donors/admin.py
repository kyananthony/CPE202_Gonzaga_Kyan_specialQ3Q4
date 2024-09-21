from django.contrib import admin
from .models import Donor, BloodType, BloodRequest

admin.site.register(Donor)
admin.site.register(BloodType)
admin.site.register(BloodRequest)
# Register your models here.
