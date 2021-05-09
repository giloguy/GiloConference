from django.db import models

# Create your models here.

class Register(models.Model): 

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250) 
    phone = models.CharField(max_length=250) 
    address = models.CharField(max_length=250)
    topic = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name 


class Program(models.Model): 
    name = models.CharField(max_length=250)
    day = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    speaker = models.ForeignKey(Register,on_delete=models.CASCADE)
    description = models.TextField(max_length=250)
    
    def __str__(self):
        return self.name


class Contact(models.Model): 
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField(max_length=250) 
    
    def __str__(self):
        return self.name