from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=75)
    
    def __str__(self):
        """returns a string representation of itself"""
        return f"You have selected student {self.first_name} {self.last_name}"