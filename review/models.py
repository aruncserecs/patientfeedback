from django.db import models

# Create your models here.



class patient(models.Model):
    FIRST_NAME=models.CharField(max_length=90, blank=True)
    LAST_NAME=models.CharField(max_length=90, blank=True)
    Gender=models.CharField(max_length=90, blank=True)
    Hospital_Name=models.CharField(max_length=90, blank=True)
    Phone=models.CharField(max_length=11)
    REVIEW=models.CharField(max_length=890, blank=True)


    class Meta:
        db_table = "patient"