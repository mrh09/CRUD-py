from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    division = models.CharField(max_length=50)

    def __str__(self):
        return self.name
# Create your models here.
