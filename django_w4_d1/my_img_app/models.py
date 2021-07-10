from django.db import models

# Create your models here.
class Hotel(models.Model):
    name=models.CharField(max_length=20)
    hotel_Main_Img=models.ImageField(upload_to='images/')