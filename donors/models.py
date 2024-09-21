from django.db import models

# Create your models here.
class BloodType(models.Model) :
    name = models.CharField(max_length = 3)

    def __str__(self):
        return self.name
class Donor (models.Model) :
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField (unique = True)
    phone_number = models.CharField (max_length = 15)
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    city = models.CharField (max_length = 100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.blood_type})'

class BloodRequest (models.Model) :
    blood_type = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    hospital = models.CharField (max_length = 200)
    date_needed = models.DateField ()

    def __str__(self):
        return f'{self.blood_type} - {self.quantity} pints needed'
