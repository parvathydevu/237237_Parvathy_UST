from django.db import models #forms.py--created a form based on models.py,actual outcome is forms
#admin-register 'Incident' model in admin.py FILE
# Create your models here

class Incident(models.Model):

    INCIDENT_TYPES = [
        ('fire', 'Fire'), 
        ('ems', 'EMS'), 
        ('traffic', 'Traffic'), 
        ('crime', 'Crime'),
        ('natural','Natural'),
    ]

    name = models.CharField(max_length=50)
    #create age model
    age = models.IntegerField(default=0)
    location = models.CharField(max_length=50)
    incident_type = models.CharField(max_length=10, choices=INCIDENT_TYPES)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.incident_type}"