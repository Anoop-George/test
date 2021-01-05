from django.db import models


class Lead(models.Model):# for CRUD operation
    name = models.CharField(max_length=100)

class Officestaff(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Teachers(models.Model):
    name=models.CharField(max_length=100)
    officestaff = models.ManyToManyField(Officestaff)
    def __str__(self):
        return self.name
    
class Parents(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Students(models.Model):
    name=models.CharField(max_length=100)
    teacher = models.ManyToManyField(Teachers)
    parent = models.OneToOneField(Parents,on_delete=models.CASCADE,default='na')
    def __str__(self):
        return self.name


    