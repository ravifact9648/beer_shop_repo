from django.db import models

# Create your models here.
class Beer(models.Model):
    name=models.CharField(max_length=30)
    taste=models.CharField(max_length=30)
    color=models.CharField(max_length=20)
    price=models.FloatField()
    def __str__(self):
        return self.name
    
    
