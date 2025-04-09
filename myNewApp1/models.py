from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=111)
    salary = models.IntegerField()
    phoneNumber = models.CharField(max_length=222)
    mailID = models.EmailField(max_length=1111)
    
    
    def __str__(self):
        return self.name
    
    