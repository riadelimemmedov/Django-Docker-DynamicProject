from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    test_score = models.FloatField()
    
    def __str__(self):
        return "{} - {}".format(self.first_name,self.last_name)