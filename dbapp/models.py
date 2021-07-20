from django.db import models

# Create your models here.

class Economic(models.Model):
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    create_date =models.CharField(max_length=100)
    vote = models.DecimalField(max_digits=20,decimal_places=5,default=0)