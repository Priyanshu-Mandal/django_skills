from django.db import models

# Create your models here.

class data(models.Model):
    name= models.CharField(max_length=50)
    contact = models.IntegerField(max_length=10)
    interest= models.TextField(max_length=300)
    