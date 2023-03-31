from django.db import models

# Create your models here.
class ContactData(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=30)
    location=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
